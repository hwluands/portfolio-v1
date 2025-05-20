# Tupla fornecida com itens e preços
t1 = ('Doce', 2.3, 'Bala', 0.15, 'Pizza', 28.9, 'Arroz', 4.5, 'Paçoca', 0.5, 'Pamonha', 5.4)

# Função para exibir o cardápio
def exibir_cardapio(tupla):
    print("-" * 30)
    print(f"{'Cardápio':^30}")  # Centraliza a palavra "Cardápio"
    print("-" * 30)

    for i in range(0, len(tupla), 2):  # Pula de dois em dois para pegar o nome do item e o preço
        item, preco = tupla[i], tupla[i + 1]
        print(f"{item:<20}: R$ {preco:>.2f}")  # Formata a string para alinhar à esquerda e formatar o preço

    print("-" * 30)

# Função para simular o atendimento ao cliente e calcular o total
def atendimento_cliente(tupla):
    total_pedido = 0.0
    carrinho = []

    while True:
        print("\nOlá! Bem-vindo ao nosso restaurante virtual. Aqui está o nosso cardápio:")
        exibir_cardapio(tupla)
        
        escolha = input("\nDigite o nome do item para adicioná-lo ao seu pedido ou 'sair' para finalizar: ").strip().title()

        if escolha.lower() == 'sair':
            print(f"\nO valor total do seu pedido é R$ {total_pedido:.2f}.")
            print("Seu pedido será preparado o mais breve possível. Agradecemos pela preferência!")
            break
        elif escolha in tupla:
            indice = tupla.index(escolha)
            preco = tupla[indice + 1]
            carrinho.append((escolha, preco))
            total_pedido += preco
            print(f"Adicionado: {escolha} pelo preço de R$ {preco:.2f}. Valor total até agora: R$ {total_pedido:.2f}.")
        else:
            print("Desculpe, não conseguimos encontrar esse item no cardápio. Por favor, tente novamente.")

# Chama a função para iniciar o atendimento ao cliente
atendimento_cliente(t1)
