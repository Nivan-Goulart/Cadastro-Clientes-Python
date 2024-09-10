def cadastrar_cliente(nome, email, telefone):
    """
    Cadastrar um novo cliente após validar o e-mail e formatar os dados.

    Parâmetros:
    nome (str): Nome do cliente.
    email (str): Endereço de e-mail do cliente.
    telefone(str): Número de telefone do cliente.

    Retorna:
    dict: Um dicionário com as informações do cliente cadastrado.
    """
    
    # Validação do e-mail
    while not ('@' in email and '.com' in email.split('@')[-1]):
        print('E-mail incorreto. \nPor favor, digite um e-mail válido com "@" e ".com".')
        email = input("Digite o e-mail do cliente: ").strip()
        print()
        
    # Criação do dicionário com as informações do cliente
    cliente = {
        'nome': nome.strip().capitalize(),
        'email': email.strip(),
        'telefone': ''.join(c for c in telefone.strip() if c.isdigit())
    }

    return cliente

# Dicionário para armazenar clientes cadastrados
clientes_cadastrados = {}

# Contador para identificar cada cadastro
contador = 1

# Mensagem de início do processo de cadastro
print("Iniciando cadastro de clientes")

# Loop principal para cadastro de clientes
while True:
    print()
    print('Cadastro de nº {}'.format(contador))

    # Entrada do nome do cliente
    nome = input('Por favor, digite o nome do cliente: (ou "sair" para encerrar): ')

    # Condição de saída do loop
    if nome.lower() == 'sair':
        break

    # Entrada do e-mail e telefone do cliente
    email = input('Por favor, digite o e-mail do contato:')
    telefone = input('Por favor, digite o telefone:')

    # Chama a função para cadastrar o cliente
    cadastro = cadastrar_cliente(nome,email,telefone)

    # Armazena o cliente no dicionário com o e-mail como chave
    clientes_cadastrados[cadastro['email']] = cadastro

    # Incrementa o contador para o próximo cadastro
    contador +=1

print()

# Exibe os clientes cadastrados 
print("Clientes cadastrados: ")
for email, cliente in clientes_cadastrados.items():
    print('E-mail: {}'.format(email))
    print('Nome: {}'.format(cliente['nome']))
    print('Telefone: {}'.format(cliente['telefone']))
    print()