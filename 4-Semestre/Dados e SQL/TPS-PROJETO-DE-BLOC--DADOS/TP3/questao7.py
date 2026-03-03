from sqlalchemy import create_engine, text

USER = "postgres"
PASSWORD = "gui123reis13"
HOST = "localhost"
PORT = "5433"
DB = "tp3-pb"
SCHEMA = "mercadinho"

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}?options=-csearch_path%3D{SCHEMA}"
)

def fetch_as_list(query: str):
    """Executa a consulta SQL e retorna uma lista de dicionários."""
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return [dict(row) for row in result.mappings().all()]

# CONSULTAS (INNER, LEFT e RIGHT JOIN)

query_inner = """
SELECT vendas.id_venda, vendas.data, vendas.valor_total, clientes.nome AS cliente
FROM vendas
INNER JOIN clientes ON clientes.id_cliente = vendas.id_cliente;
"""

query_left = """
SELECT produtos.nome AS produto, itens_venda.quantidade, vendas.data
FROM produtos
LEFT JOIN itens_venda ON produtos.id_produto = itens_venda.id_produto
LEFT JOIN vendas ON itens_venda.id_venda = vendas.id_venda;
"""

query_right = """
SELECT produtos.nome AS produto, itens_venda.quantidade, vendas.data
FROM produtos
RIGHT JOIN itens_venda ON produtos.id_produto = itens_venda.id_produto
RIGHT JOIN vendas ON itens_venda.id_venda = vendas.id_venda;
"""

# POPULANDO AS LISTAS COM OS RESULTADOS

lista_inner = fetch_as_list(query_inner)
lista_left = fetch_as_list(query_left)
lista_right = fetch_as_list(query_right)

# IMPRESSÃO DAS LISTAS (opcional, apenas para visualizar)

print("\n Lista INNER JOIN — Vendas com Cliente:")
for item in lista_inner:
    print(item)

print("\n Lista LEFT JOIN — Produtos e possíveis vendas:")
for item in lista_left:
    print(item)

print("\n Lista RIGHT JOIN — Itens de venda garantidos:")
for item in lista_right:
    print(item)
