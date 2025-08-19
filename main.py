from despesas_controller import adicionar_despesa, listar_despesas, total_despesas

def menu():
    while True:
        print("\nControle de Despesas")
        print("1 - Adicionar despesa")
        print("2 - Listar despesas")
        print("3 - Ver total")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome da despesa: ")
            valor = float(input("Valor da despesa: "))
            adicionar_despesa(nome, valor)
            print("Despesa adicionada!")
        elif escolha == "2":
            listar_despesas()
        elif escolha == "3":
            print(f"Total: R${total_despesas():.2f}")
        elif escolha == "4":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()

