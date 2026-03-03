


CREATE SCHEMA IF NOT EXISTS mercadinho;

-- TABELA: CLIENTES
CREATE TABLE clientes (
id_cliente SERIAL PRIMARY KEY,
nome VARCHAR(150) NOT NULL,
cpf VARCHAR(14) UNIQUE,
telefone VARCHAR(20),
endereco VARCHAR(255)
);

-- TABELA: FORNECEDORES
CREATE TABLE fornecedores (
id_fornecedor SERIAL PRIMARY KEY,
nome VARCHAR(150) NOT NULL,
cnpj VARCHAR(18) UNIQUE,
telefone VARCHAR(20)
);

-- TABELA: PRODUTOS
CREATE TABLE produtos (
id_produto SERIAL PRIMARY KEY,
nome VARCHAR(150) NOT NULL,
categoria VARCHAR(100),
preco NUMERIC(10,2) NOT NULL,
estoque INTEGER DEFAULT 0,
id_fornecedor INTEGER NOT NULL,

CONSTRAINT fk_produto_fornecedor
FOREIGN KEY (id_fornecedor)
REFERENCES fornecedores (id_fornecedor)
ON UPDATE CASCADE
ON DELETE RESTRICT
);

-- TABELA: VENDAS
CREATE TABLE vendas (
id_venda SERIAL PRIMARY KEY,
data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
valor_total NUMERIC(10,2),
id_cliente INTEGER NOT NULL,

CONSTRAINT fk_venda_cliente
FOREIGN KEY (id_cliente)
REFERENCES clientes (id_cliente)
ON UPDATE CASCADE
3
ON DELETE RESTRICT
);

-- TABELA: ITENS DA VENDA
CREATE TABLE itens_venda (
id_item SERIAL PRIMARY KEY,
quantidade INTEGER NOT NULL,
preco_unitario NUMERIC(10,2) NOT NULL,
id_venda INTEGER NOT NULL,
id_produto INTEGER NOT NULL,

CONSTRAINT fk_item_venda
FOREIGN KEY (id_venda)
REFERENCES vendas (id_venda)
ON UPDATE CASCADE
ON DELETE CASCADE,

CONSTRAINT fk_item_produto
FOREIGN KEY (id_produto)
REFERENCES produtos (id_produto)
ON UPDATE CASCADE
ON DELETE RESTRICT
);

-- ÍNDICES (OPCIONAIS, melhora performance)
CREATE INDEX idx_produtos_fornecedor ON produtos(id_fornecedor);
CREATE INDEX idx_vendas_cliente ON vendas(id_cliente);
CREATE INDEX idx_itens_venda_produto ON itens_venda(id_produto);
CREATE INDEX idx_itens_venda_venda ON itens_venda(id_venda);


-- INSERTS DE DADOS

INSERT INTO mercadinho.fornecedores (nome, cnpj, telefone)
VALUES
('Alimentos Silva LTDA', '12.345.678/0001-90', '(71) 98888-1122'),
('Distribuidora Central', '98.765.432/0001-55', '(71) 97777-2211'),
('Bebidas Premium S.A', '21.345.998/0001-33', '(71) 96666-3344');

INSERT INTO mercadinho.produtos (nome, categoria, preco, estoque, id_fornecedor)
VALUES
('Arroz 5kg', 'Alimentos', 22.50, 40, 1),
('Feijão 1kg', 'Alimentos', 8.99, 80, 1),
('Macarrão 500g', 'Massas', 4.79, 60, 1),
('Refrigerante 2L', 'Bebidas', 7.50, 100, 3),
('Água Mineral 500ml', 'Bebidas', 2.00, 150, 3),
4
('Sabonete Neutro', 'Higiene', 3.50, 90, 2);

INSERT INTO mercadinho.clientes (nome, cpf, telefone, endereco)
VALUES
('Maria Souza', '123.456.789-10', '(71) 99111-2222', 'Rua A, 120'),
('João Pereira', '987.654.321-00', '(71) 99222-3333', 'Rua B, 450'),
('Guilherme Reis', '555.444.333-22', '(71) 99333-4444', 'Rua C, 250');

INSERT INTO mercadinho.vendas (valor_total, id_cliente)
VALUES
(45.99, 1),
(18.29, 2),
(10.00, 3);

INSERT INTO mercadinho.itens_venda (quantidade, preco_unitario, id_venda, id_produto)
VALUES
(1, 22.50, 1, 1),
(1, 8.99, 1, 2),
(1, 7.50, 1, 4),
(2, 4.79, 2, 3),
(1, 8.99, 2, 2),
(5, 2.00, 3, 5);

-- a) INNER JOIN - Mostrar vendas com os produtos vendidos
SELECT
v.id_venda,
c.nome AS cliente,
p.nome AS produto,
i.quantidade,
i.preco_unitario
FROM mercadinho.vendas v
INNER JOIN mercadinho.clientes c ON c.id_cliente = v.id_cliente
INNER JOIN mercadinho.itens_venda i ON i.id_venda = v.id_venda
INNER JOIN mercadinho.produtos p ON p.id_produto = i.id_produto;

-- b) LEFT JOIN - Listar todos os produtos, mesmo os que ainda não foram vendidos
SELECT
p.nome AS produto,
p.estoque,
i.quantidade,
i.id_venda
FROM mercadinho.produtos p
LEFT JOIN mercadinho.itens_venda i ON p.id_produto = i.id_produto;

-- c) RIGHT JOIN - Listar vendas com seus itens (mesmo se um produto não estiver
cadastrado)
SELECT
v.id_venda,
i.id_item,
p.nome AS produto
FROM mercadinho.produtos p
RIGHT JOIN mercadinho.itens_venda i ON p.id_produto = i.id_produto
RIGHT JOIN mercadinho.vendas v ON i.id_venda = v.id_venda;