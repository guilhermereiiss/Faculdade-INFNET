
import { FaDiscord, FaGithub, FaInstagram, FaLinkedin } from 'react-icons/fa';
import styles from './Footer.module.css';

const Footer = () => {
    return (
        <footer className={styles.footer}>
            <div className={styles.iconContainer}>
                <a href="https://discord.gg/GcKPYtpEPE" target="_blank" rel="discord" className={styles.icon}>
                    <FaDiscord />
                </a>
                <a href="https://github.com/guilhermereiiss" target="_blank" rel="github" className={styles.icon}>
                    <FaGithub />
                </a>
                <a href="https://www.instagram.com/http_guireis/" target="_blank" rel="insta" className={styles.icon}>
                    <FaInstagram />
                </a>
                <a href="https://www.linkedin.com/in/guilherme-reis-d3v/" target="_blank" rel="linkedin" className={styles.icon}>
                    <FaLinkedin />
                </a>
            </div>
            <p className={styles.copyright}>
                &copy; {new Date().getFullYear()} Guilherme Reis. Todos os direitos reservados.
            </p>
        </footer>
    );
};

export default Footer;
