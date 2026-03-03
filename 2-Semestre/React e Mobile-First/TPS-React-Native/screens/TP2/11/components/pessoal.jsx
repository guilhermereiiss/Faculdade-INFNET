import { View, Text, StyleSheet} from "react-native-web"

const pessoal = () => {
  return (
    <View style={styles.card}>
      <Text style={{fontSize: 20, fontWeight: 'bold'}}>Sobre Mim</Text>
      <Text>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet libero sunt, corrupti reprehenderit blanditiis incidunt accusantium et iusto odio nihil quae placeat dicta quasi porro sed quo! Corrupti, labore eaque. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Pariatur, quo illo non quaerat nam ipsam ducimus, asperiores harum assumenda, iure culpa consequuntur ipsum quod praesentium? Maxime maiores esse totam corrupti. Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus dolorem consequuntur accusamus facere sit, dicta delectus distinctio perspiciatis eos ipsam voluptas excepturi, consequatur veniam, quia sed molestias soluta nihil magni?</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  card:{
    backgroundColor: '#f0f0f0',
    padding: 20,
    marginVertical: 10,
    width: '100%',
    height: '100%',
    alignItems: 'center',
  }
})

export default pessoal