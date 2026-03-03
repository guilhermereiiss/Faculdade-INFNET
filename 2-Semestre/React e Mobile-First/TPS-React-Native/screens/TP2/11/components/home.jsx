
import { View, Text, Image, StyleSheet } from 'react-native';
import FacebookIcon from '@mui/icons-material/Facebook';
import InstagramIcon from '@mui/icons-material/Instagram';
import TwitterIcon from '@mui/icons-material/Twitter';
import LinkedInIcon from '@mui/icons-material/LinkedIn';

const Home = () => {
    return (
        <View style={styles.card}>

            <Image
                source={{ uri: 'https://www.pontikis.net/wp-content/uploads/2020/06/code.png' }} // URL do banner
                style={styles.banner}
            />
            <View style={styles.card2}>
                <Text style={styles.name}>Guilherme Reis</Text>
                <Text style={styles.address}>Rua Ciclano do Fulano</Text>
                <Text style={styles.email}>guilherme.reis@email.com</Text>
                <Text style={styles.phone}>(##) #####-####</Text>
                <Text style={styles.bio}>
                    Desenvolvedor apaixonado por tecnologia, sempre buscando aprender e evoluir!
                </Text>
            </View>
            <View style={styles.socialIcons}>
                <FacebookIcon fontSize="large" style={{ color: '#4267B2', marginHorizontal: 10 }} />
                <InstagramIcon fontSize="large" style={{ color: '#E1306C', marginHorizontal: 10 }} />
                <TwitterIcon fontSize="large" style={{ color: '#1DA1F2', marginHorizontal: 10 }} />
                <LinkedInIcon fontSize="large" style={{ color: '#0077B5', marginHorizontal: 10 }} />
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    card: {
        backgroundColor: '#fff',

        elevation: 5,
        marginVertical: 10,
        width: '100%',
        height: '100%',
        alignSelf: 'center',
    },
    card2: {
        alignItems: 'flex-start',
        padding: 20,
    },
    banner: {
        width: '100%',
        height: 180,
        marginBottom: 10,
    },
    name: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#333',
        marginVertical: 5,
        textAlign: 'center',
    },
    address: {
        fontSize: 16,
        color: '#666',
        textAlign: 'center',
        marginVertical: 5,
    },
    email: {
        fontSize: 16,
        color: '#666',
        textAlign: 'center',
        marginBottom: 5,
    },
    phone: {
        fontSize: 16,
        color: '#666',
        textAlign: 'center',
        marginBottom: 10,
    },
    bio: {
        fontSize: 14,
        color: '#777',
        marginBottom: 15,
    },
    socialIcons: {
        flexDirection: 'row',
        justifyContent: 'center',
    },
});

export default Home;
