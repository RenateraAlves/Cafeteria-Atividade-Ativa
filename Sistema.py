# Coffee Shops Tia Rosa - Sistema Simples

# --- Parte 1: Cardápio e Pedidos ---

# Cardápio com produtos e preços
Cardápio = {
    '1': {'nome': 'Café', 'valor': 2.50},
    '2': {'nome': 'Café com Leite', 'valor': 3.50},
    '3': {'nome': 'Café Expresso', 'valor': 6.00},
    '4': {'nome': 'Pão de Queijo', 'valor': 3.50},
    '5': {'nome': 'Bolo do Dia (Fatia)', 'valor': 5.00},
    '6': {'nome': 'Torta de Frango', 'valor': 7.00},
    '7': {'nome': 'Água Mineral', 'valor': 3.00},
    '8': {'nome': 'Refrigerante Lata', 'valor': 3.50}
}

Pedidos = []  # Lista para armazenar pedidos

# Função para listar produtos do cardápio
def Lista_De_Produtos():
    print('\n----- Cardápio -----')
    for codigo in Cardápio:
        produto = Cardápio[codigo]
        print(codigo + '. ' + produto['nome'] + ' - R$ ' + str(produto['valor']))

# Função para fazer pedidos
def Fazer_Pedido():
    while True:
        print('\nDigite o código do produto:')
        codigo = input()
        if codigo == '0':
            break
        if codigo not in Cardápio:
            print('Código inválido, tente novamente.')
            continue
        print('Digite a quantidade:')
        try:
            quantidade = int(input())
        except:
            print('Quantidade inválida, tente novamente.')
            continue
        pedido = {
            'produto': Cardápio[codigo]['nome'],
            'quantidade': quantidade,
            'valor': Cardápio[codigo]['valor'] * quantidade
        }
        Pedidos.append(pedido)
        print('Adicionado ' + str(quantidade) + 'x ' + pedido['produto'] + ' ao pedido.')

# Função para mostrar pedidos feitos
def Mostrar_Pedidos():
    if len(Pedidos) == 0:
        print('Nenhum pedido feito.')
        return
    print('\nPedidos feitos:')
    total = 0
    for pedido in Pedidos:
        print(str(pedido['quantidade']) + 'x ' + pedido['produto'] + ' - R$ ' + str(pedido['valor']))
        total += pedido['valor']
    print('Total: R$ ' + str(total))

# Menu do Cardápio e Pedidos
def menu_cardapio_pedidos():
    while True:
        print('\n----- Menu Cardápio e Pedidos -----')
        print('1. Listar Produtos')
        print('2. Listar Pedidos')
        print('3. Fazer Pedidos')
        print('4. Voltar')
        escolha = input('Selecione a opção desejada: ')
        if escolha == '1':
            Lista_De_Produtos()
        elif escolha == '2':
            Mostrar_Pedidos()
        elif escolha == '3':
            Fazer_Pedido()
        elif escolha == '4':
            break
        else:
            print('Opção inválida, tente novamente.')

# --- Parte 2: Cadastro de Clientes ---

# Dicionário para guardar clientes
cadastro_clientes = {}

# Função para mostrar menu de clientes
def exibir_menu_clientes():
    print("\n----- Cadastro de Clientes -----")
    print("1. Adicionar Cliente")
    print("2. Listar Clientes")
    print("3. Remover Cliente")
    print("4. Voltar")

# Função para adicionar cliente
def adicionar_cliente():
    nome_cliente = input('\nDigite o nome do cliente: ')
    telefone_cliente = input('Digite o telefone do cliente: ')
    if not nome_cliente:
        print('\nDigite um nome válido.')
    elif not telefone_cliente:
        print('Digite um telefone válido.')
    elif not telefone_cliente.isdigit() or len(telefone_cliente) < 8:
        print('\nO telefone deve conter apenas números e ter pelo menos 8 dígitos.')
    else:
        cadastro_clientes[nome_cliente] = telefone_cliente
        print(f'Cliente {nome_cliente.title()} cadastrado com sucesso.')

# Função para listar clientes
def listar_clientes():
    if cadastro_clientes:
        print('\nClientes cadastrados:')
        for nome, telefone in cadastro_clientes.items():
            print(f'Cliente: {nome.title()} \nTelefone: {telefone}\n')
    else:
        print('\nNão existem clientes cadastrados!')

# Função para remover cliente
def remover_cliente():
    nome = input('\nDigite o nome do cliente que deseja remover: ')
    if nome in cadastro_clientes:
        del cadastro_clientes[nome]
        print(f'{nome.title()} removido do sistema!')
    else:
        print('\nNome informado está incorreto ou não existe no sistema.')

# Menu de clientes
def menu_clientes():
    while True:
        exibir_menu_clientes()
        escolha = input('Selecione a opção desejada: ')
        if escolha == '1':
            adicionar_cliente()
        elif escolha == '2':
            listar_clientes()
        elif escolha == '3':
            remover_cliente()
        elif escolha == '4':
            break
        else:
            print('Opção inválida, tente novamente.')

# --- Parte Inicial do Sistema ---

def menu_principal():
    print('Coffee Shops Tia Rosa\n')
    print('Sejam Bem Vindos Ao Coffee Shops Tia Rosa')
    while True:
        print('\n----- Menu Principal -----')
        print('1. Cardápio e Pedidos')
        print('2. Cadastro de Clientes')
        print('3. Sair')
        escolha = input('Selecione a opção desejada: ')
        if escolha == '1':
            menu_cardapio_pedidos()
        elif escolha == '2':
            menu_clientes()
        elif escolha == '3':
            print('Saindo do sistema... Obrigado!')
            break
        else:
            print('Opção inválida, tente novamente.')

# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()
