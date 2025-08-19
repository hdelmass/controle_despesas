import json

ARQUIVO = "database.json"

def carregar_despesas():
    try:
        with open(ARQUIVO, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_despesas(despesas):
    with open(ARQUIVO, "w") as file:
        json.dump(despesas, file, indent=4)

def adicionar_despesa(nome, valor):
    despesas = carregar_despesas()
    despesas.append({"nome": nome, "valor": valor})
    salvar_despesas(despesas)

def listar_despesas():
    despesas = carregar_despesas()
    if not despesas:
        print("Nenhuma despesa registrada.")
        return
    for i, d in enumerate(despesas, start=1):
        print(f"{i}. {d['nome']} - R${d['valor']:.2f}")

def total_despesas():
    despesas = carregar_despesas()
    return sum(d['valor'] for d in despesas)
