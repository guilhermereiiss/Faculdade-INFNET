
-- 1) Ativar o schema mercadinho
SET search_path TO mercadinho;

-- 2) Criar a tabela categoria (se ainda não existir)
CREATE TABLE IF NOT EXISTS categoria (
    id_categoria SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

-- 3) Popular com as categorias que você já está usando nos produtos
INSERT INTO categoria (nome) VALUES 
('Alimentos'),
('Massas'),
('Bebidas'),
('Higiene')
ON CONFLICT (nome) DO NOTHING;


-- 4) Adicionar a coluna id_categoria na tabela produtos
ALTER TABLE produtos 
ADD COLUMN IF NOT EXISTS id_categoria INTEGER;

-- 5) Preencher automaticamente a chave estrangeira com base no texto atual
UPDATE produtos SET id_categoria = c.id_categoria
FROM categoria c
WHERE TRIM(UPPER(produtos.categoria)) = TRIM(UPPER(c.nome))
  AND produtos.id_categoria IS NULL;

-- 6) Tornar a coluna NOT NULL e criar a FK
ALTER TABLE produtos ALTER COLUMN id_categoria SET NOT NULL;

ALTER TABLE produtos 
ADD CONSTRAINT fk_produto_categoria 
FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
ON UPDATE CASCADE ON DELETE RESTRICT;

