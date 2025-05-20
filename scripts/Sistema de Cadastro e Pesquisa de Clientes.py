# Definindo uma lista para armazenar as informações dos clientes
clientes = []

# Função para cadastrar um novo cliente
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    idade = input("Digite a idade do cliente: ")
    # Adicionando as informações em um dicionário e armazenando na lista de clientes
    clientes.append({"nome": nome, "email": email, "telefone": telefone, "idade": idade})
    print("Cliente cadastrado com sucesso!")

# Função para buscar e mostrar informações do cliente pelo email
def buscar_cliente():
    email_busca = input("Digite o email do cliente para busca: ")
    # Procurando o cliente na lista de clientes
    for cliente in clientes:
        if cliente['email'] == email_busca:
            print("Informações do Cliente:")
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Idade: {cliente['idade']}")
            return
    print("Cliente não encontrado!")

# Interface do sistema
def sistema():
    while True:
        print("\nSistema de Cadastro e Pesquisa de Clientes")
        print("1. Cadastrar Cliente")
        print("2. Buscar Cliente")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            buscar_cliente()
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")

# Executando o sistema
sistema()
