import { useState, useEffect } from 'react';
import { View, FlatList, StyleSheet, ActivityIndicator, RefreshControl, Button, } from 'react-native';
import NewsCard from '../NewsCard/index.jsx';
import SearchBar from '../SearchBar/index.jsx';
import { fetchNews } from '../../services/index.jsx';

const NewsListScreen = () => {
    const [newsList, setNewsList] = useState([]);
    const [loading, setLoading] = useState(false);
    const [refreshing, setRefreshing] = useState(false);
    const [query, setQuery] = useState('');
    const [page, setPage] = useState(1);
    const [sortBy, setSortBy] = useState('titulo');

    const loadNews = async (isRefreshing = false) => {
        if (!isRefreshing) setLoading(true);

        const params = {
            busca: query,
            ordenacao: sortBy,
            pagina: page,
        };

        const data = await fetchNews(params);
        setNewsList(isRefreshing ? data : [...newsList, ...data]);

        setLoading(false);
        setRefreshing(false);
    };

    useEffect(() => {
        loadNews(true);
    }, [query, sortBy]);

    const handleLoadMore = () => {
        setPage(page + 1);
    };

    const handleRefresh = () => {
        setPage(1);
        setRefreshing(true);
        loadNews(true);
    };

    return (
        <View style={styles.container}>
            <SearchBar query={query} setQuery={setQuery} />
            <Button style={styles.butn} title="Ordenação por Titulo" onPress={() => setSortBy('titulo')}  />
            <FlatList
                data={newsList}
                keyExtractor={(item) => item.id}
                renderItem={({ item }) => <NewsCard news={item} />}
                onEndReached={handleLoadMore}
                onEndReachedThreshold={0.1}
                ListFooterComponent={loading && <ActivityIndicator />}
                refreshControl={
                    <RefreshControl refreshing={refreshing} onRefresh={handleRefresh} />
                }
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f9f9f9',
    },
    butn:{
        backgroundColor: '#32CD32',
    }
});

export default NewsListScreen;
