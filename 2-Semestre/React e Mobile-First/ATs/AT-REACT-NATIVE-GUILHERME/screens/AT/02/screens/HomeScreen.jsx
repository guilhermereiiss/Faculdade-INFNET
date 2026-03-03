

import { useState, useEffect } from 'react';
import { View, FlatList, StyleSheet, RefreshControl, Text } from 'react-native';
import { fetchAstroImages } from '../api/nasaApi';
import ImageCard from '../components/ImageCard';
import AstroSelector from '../components/AstroSelector';
import LoadingIndicator from '../components/LoadingIndicator';

const HomeScreen = ({ navigation }) => {
  const [images, setImages] = useState([]);
  const [astro, setAstro] = useState('earth');
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);
  const [refreshing, setRefreshing] = useState(false);
  const [progress, setProgress] = useState(0);  
  const [totalItems, setTotalItems] = useState(0);
  const [loadedItems, setLoadedItems] = useState(0);

  useEffect(() => {
    loadImages(true); 
  }, [astro]);

  const loadImages = async (refresh = false) => {
    if (loading) return;
    setLoading(true);
    setProgress(0.1);  

    const { items, totalItems: fetchedTotalItems } = await fetchAstroImages(astro, refresh ? 1 : page);

    setTotalItems(fetchedTotalItems);
    const newLoadedItems = refresh ? items.length : loadedItems + items.length; 
    setLoadedItems(newLoadedItems);

    setProgress(1);  

    setImages(refresh ? items : [...images, ...items]);
    setPage(refresh ? 2 : page + 1);
    setLoading(false);
  };

  const onRefresh = async () => {
    setRefreshing(true);
    setLoadedItems(0); 
    await loadImages(true);
    setRefreshing(false);
  };

  return (
    <View style={styles.container}>
      <AstroSelector onAstroChange={(selected) => setAstro(selected)} />
      
      {totalItems > 0 && (
        <View style={styles.progressContainer}>
          <Text style={styles.progressText}>
            {Math.round((loadedItems / totalItems) * 100)}% Carregado
          </Text>
          <View style={styles.progressBarContainer}>
            <View style={[styles.progressBar, { width: `${(loadedItems / totalItems) * 100}%` }]} />
          </View>
        </View>
      )}

      <FlatList
        data={images}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <ImageCard
            item={item}
            onPress={() => navigation.navigate('ImageDetails', { item })}
          />
        )}
        onEndReached={() => loadImages()} 
        onEndReachedThreshold={0.5}
        refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} />}
        ListFooterComponent={() => loading && <LoadingIndicator progress={progress} />}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: '#101526',   
  },
  progressContainer: {
    marginBottom: 10,
    alignItems: 'center',
  },
  progressText: {
    fontSize: 16,
    marginBottom: 5,
    color: '#FFFF', 
  },
  progressBarContainer: {
    width: '100%',
    height: 10,
    backgroundColor: '#05070D',  
    borderRadius: 5,
    overflow: 'hidden',
  },
  progressBar: {
    height: '100%',
    backgroundColor: '#1A6DD9', 
  },
});

export default HomeScreen;
