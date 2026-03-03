# 🎬 MatchMovie

## 📌 Visão Geral
MatchMovie é uma aplicação web desenvolvida em **React.js** com **Vite**, projetada para fornecer recomendações personalizadas de filmes com base no histórico de visualização e preferências do usuário. O projeto integra a **API TMDb** para exibição de dados detalhados sobre os filmes, incluindo avaliações, trailers e categorias.

## 🚀 Tecnologias e Ferramentas Utilizadas
- **React.js** (Framework principal)
- **Vite** (Otimização e build)
- **React Router** (Gerenciamento de rotas)
- **Styled Components** (Estilização dinâmica)
- **Axios** (Consumo de APIs)
- **TMDb API** (Fonte de dados sobre filmes)
- **LocalStorage** (Persistência de dados do usuário)

## 📂 Estrutura do Projeto
```
MatchMovie/
│── src/
│   ├── components/      # Componentes reutilizáveis
│   ├── pages/           # Páginas principais da aplicação
│   ├── routes/          # Configuração de rotas
│   ├── services/        # Comunicação com APIs externas
│   ├── assets/          # Recursos estáticos (imagens, ícones)
│   ├── hooks/           # Hooks personalizados
│   ├── contexts/        # Gerenciamento de estado global
│   ├── styles/          # Estilos globais e temas
│   ├── utils/           # Funções auxiliares e helpers
│── public/              # Arquivos públicos
│── package.json         # Dependências do projeto
│── vite.config.js       # Configuração do Vite
│── README.md            # Documentação do projeto
```

## 🔗 Navegação e Rotas
| Rota               | Componente         | Descrição |
|--------------------|------------------|------------|
| `/`                | Home             | Página inicial com recomendações personalizadas |
| `/filme/:id`       | MovieDetails     | Detalhes do filme selecionado |
| `/favoritos`       | Favorites        | Listagem de filmes favoritos |
| `/buscar`          | Search           | Mecanismo de busca por filmes |
| `/perfil`          | Profile          | Gerenciamento do perfil do usuário |
| `*`                | NotFound         | Página de erro 404 |

## ⚡ Como Executar o Projeto
### Pré-requisitos
- **Node.js** instalado
- **Gerenciador de pacotes npm ou yarn**

### Passos para instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/MatchMovie.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd MatchMovie
   ```
3. Instale as dependências:
   ```bash
   npm install
   ```
4. Execute o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```
5. Acesse no navegador:
   ```
   http://localhost:5173
   ```

## 🛠️ Principais Funcionalidades
- 🔥 **Recomendações personalizadas** baseadas no histórico do usuário
- 🔍 **Busca avançada** por filmes e categorias
- ⭐ **Gerenciamento de favoritos**
- 🎥 **Exibição de trailers** diretamente na interface
- 📊 **Classificação e avaliações** extraídas da API TMDb
- 🌓 **Modo claro e escuro** para melhor experiência do usuário

## 🎯 Contribuição
Se deseja contribuir para o projeto, siga os passos abaixo:
1. Faça um fork do repositório
2. Crie uma branch para a nova funcionalidade (`git checkout -b feature-nova-funcionalidade`)
3. Implemente as alterações e faça commit (`git commit -m 'Descrição das mudanças'`)
4. Faça o push para o seu repositório (`git push origin feature-nova-funcionalidade`)
5. Abra um Pull Request para análise

## 📜 Licença
Este projeto está sob a licença **MIT**, permitindo seu uso, modificação e distribuição livremente.

---

Desenvolvido por **Guilherme Reis** 🚀

