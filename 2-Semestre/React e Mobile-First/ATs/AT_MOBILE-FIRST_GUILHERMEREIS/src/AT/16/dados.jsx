const dados = {
    produto: {
        nome: 'Produto Exemplo',
        imagem: 'https://placehold.co/400',
        descricao: 'Descrição do produto.',
        preco: .00,
        nota: 4.5,
    },
    vendedor: {
        nome: 'Vendedor Exemplo',
        email: 'vendedor@example.com',
        telefone: '1234-5678',
        nota: 4.8,
    },
    comentarios: [
        {
            nomeUsuario: 'Usuário 1',
            data: '2024-09-20',
            mensagem: 'Ótimo produto!',
            nota: 5,
        },
        {
            nomeUsuario: 'Usuário 2',
            data: '2023-04-20',
            mensagem: 'Ótimo atendimento!',
            nota: 5,
        },
        {
            nomeUsuario: 'Usuário 3',
            data: '2023-05-12',
            mensagem: 'Achei mais ou menos!',
            nota: 3,
        },
    ],
    perguntas: [
        {
            nomeUsuario: 'Usuário 2',
            data: '2024-09-21',
            duvida: 'Esse produto é à prova d\'água?',
            resposta: 'Sim, ele é à prova d\'água.',
        },
        {
            nomeUsuario: 'Usuário 3',
            data: '2024-09-22',
            duvida: 'Esse produto tem garantia?',
            resposta: 'Sim, o produto possui garantia de 1 ano.',
        },
        {
            nomeUsuario: 'Usuário 4',
            data: '2024-09-23',
            duvida: 'Qual é a voltagem do produto?',
            resposta: 'O produto é bivolt, funcionando tanto em 110V quanto em 220V.',
        },
        
    ],
    produtosRelacionados: [
        {
            nome: 'Produto Relacionado 1',
            imagem: 'https://placehold.co/100',
            preco: 80.00,
        },
        {
            nome: 'Produto Relacionado 2',
            imagem: 'https://placehold.co/100',
            preco: 120.00,
        },
        {
            nome: 'Produto Relacionado 3',
            imagem: 'https://placehold.co/100',
            preco: 150.00,
        },
    ],
};

export default dados;

