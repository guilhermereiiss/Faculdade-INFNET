import { Card, CardMedia, CardContent, Typography, CardActions, IconButton, Avatar } from '@mui/material';
import { Favorite, Share, Comment } from '@mui/icons-material';
import listaComentarios from './CommentList';
import styles from './Post.module.css'; 


export default function Post({ post }) {
    return (
        <Card className={styles.card}>
            <CardMedia
                component="img"
                height="140"
                image={post.image}
                alt={post.title}
                className={styles.imagemCard}
            />
            <CardContent className={styles.conteudoCard}>
                <div className={styles.cabecalhoPost}>
                    <Avatar alt={post.autor} src={post.avatar} className={styles.avatarAutor} />
                    <div>
                        <Typography variant="h6" className={styles.tituloPost}>{post.title}</Typography>
                        <Typography variant="caption" className={styles.dataPost}>{post.date}</Typography>
                    </div>
                </div>
                <Typography variant="body2" className={styles.textooPost}>{post.texto}</Typography>
            </CardContent>
            <CardActions className={styles.acoesCard}>
                <IconButton aria-label="like" className={styles.botaoAcao}>
                    <Favorite /> {post.likes}
                </IconButton>
                <IconButton aria-label="share" className={styles.botaoAcao}>
                    <Share /> {post.compartilhar}
                </IconButton>
                <IconButton aria-label="comment" className={styles.botaoAcao}>
                    <Comment />
                </IconButton>
            </CardActions>
            <listaComentarios comentarios={post.comentarios} />
        </Card>
    );
}
