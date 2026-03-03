import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const navigate = useNavigate();

    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');
    const [error, setError] = useState('');

    const handleLogin = () => {
        const storedEmail = localStorage.getItem('email');
        const storedSenha = localStorage.getItem('senha');

        if (email === storedEmail && senha === storedSenha) {
            navigate("/MatchMovie/home");
        } else {
            setError('Email ou senha incorretos');
        }
    };

    return (
        <div style={{ 
            backgroundColor: 'var(--cor-primaria)', 
            height: '100vh', 
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center', 
            flexDirection: 'column' 
        }}>

            <div style={{ 
                color: 'var(--cor-card)',
                fontWeight: 'bold', 
                marginBottom: '1rem', 
                textAlign: 'center' 
            }}>
                <p>ADICIONE NO SEU CONSOLE:</p>
                <p>localStorage.setItem('email', 'seuemail@exemplo.com')</p>
                <p>localStorage.setItem('senha', 'suasenha123')</p>
            </div>
            
            <div style={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                flexDirection: 'column',
                maxWidth: '400px',
                width: '100%',
                padding: '2rem',
                boxShadow: 'var(--sombra-card)',
                borderRadius: '8px',
                textAlign: 'center',
                backgroundColor: 'var(--cor-card)',
            }}>
                <h4 style={{ color: 'var(--cor-card-text)', fontWeight: 'bold' }}>Entre em sua conta</h4>
                <p style={{ color: 'var(--cor-button-hover)', marginBottom: '1rem' }}>Bem vindo! Faça login para continuar.</p>

                <input
                    type="email"
                    placeholder="Email"
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    style={{
                        width: '100%',
                        padding: '10px',
                        marginBottom: '1rem',
                        borderRadius: '4px',
                        border: '1px solid #ccc'
                    }}
                />

                <input
                    type="password"
                    placeholder="Senha"
                    required
                    value={senha}
                    onChange={(e) => setSenha(e.target.value)}
                    style={{
                        width: '100%',
                        padding: '10px',
                        marginBottom: '1rem',
                        borderRadius: '4px',
                        border: '1px solid #ccc'
                    }}
                />

                {error && <p style={{ color: 'red', marginBottom: '1rem' }}>{error}</p>}
                
                <button
                    onClick={handleLogin}
                    style={{
                        width: '100%',
                        padding: '12px',
                        backgroundColor: 'var(--cor-botao)',
                        color: 'var(--cor-botao-texto)',
                        borderRadius: '4px',
                        border: 'none',
                        fontSize: '1rem',
                        cursor: 'pointer',
                        marginBottom: '1rem',
                        transition: 'background-color 0.3s',
                    }}
                    onMouseOver={(e) => e.target.style.backgroundColor = 'var(--cor-button-hover)'}
                    onMouseOut={(e) => e.target.style.backgroundColor = 'var(--cor-botao)'}
                >
                    Entrar
                </button>

            </div>
        </div>
    );
};

export default Login;
