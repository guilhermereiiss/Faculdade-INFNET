
from sqlalchemy import create_engine, text

USER = "postgres"
PASSWORD = "gui123reis13"
HOST = "localhost"
PORT = "5433"
DB = "tp3-pb"
SCHEMA = "mercadinho"

DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    f"?options=-csearch_path%3D{SCHEMA}"
)

engine = create_engine(DATABASE_URL)

def executar_consulta(sql):
    with engine.connect() as conn:
        resultado = conn.execute(sql)
        return [dict(row) for row in resultado.mappings()]

# CONSULTAS DQL (item 4)
sql_inner = text("""
    SELECT c.nome AS cliente, c.telefone, v.data, v.valor_total
    FROM clientes c
    INNER JOIN vendas v ON c.id_cliente = v.id_cliente
    ORDER BY v.data;
""")

sql_left = text("""
    SELECT cat.nome AS categoria, p.nome AS produto
    FROM categoria cat
    LEFT JOIN produtos p ON cat.id_categoria = p.id_categoria
    ORDER BY cat.nome;
""")

sql_right = text("""
    SELECT p.nome AS produto, cat.nome AS categoria
    FROM produtos p
    RIGHT JOIN categoria cat ON p.id_categoria = cat.id_categoria
    ORDER BY cat.nome;
""")

# EXECUÇÃO E POPULAÇÃO (itens 5 e 7) 

# Item 5: populando dicionários (na verdade listas de dicionários)
print("EXECUTANDO CONSULTAS E POPULANDO ESTRUTURAS...\n")

lista_dict_inner = executar_consulta(sql_inner)   
lista_dict_left  = executar_consulta(sql_left)    
lista_dict_right = executar_consulta(sql_right)  

# Item 7: populando listasd
lista_inner = lista_dict_inner   
lista_left  = lista_dict_left
lista_right = lista_dict_right

# EXIBIÇÃO DOS RESULTADOS (itens 6 e 8) 

print("="*60)
print("INNER JOIN - Clientes que realizaram compras".center(60))
print("="*60)
for item in lista_inner:        
    print(item)

print("\n" + "="*60)
print("LEFT JOIN - Todas as categorias (mesmo sem produtos)".center(60))
print("="*60)
for item in lista_left:
    print(item)

print("\n" + "="*60)
print("RIGHT JOIN - Todas as categorias (mesmo sem produtos associados)".center(60))
print("="*60)
for item in lista_right:
    print(item)

print("\nFim da execução da questões de 5 até a 8")