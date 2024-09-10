# Cadastro de Clientes

Este projeto é um sistema simples para cadastro de clientes, que valida os dados de e-mail e formata o número de telefone automaticamente, armazenando as informações dos clientes em um dicionário.

## Funcionalidades

- **Cadastro de clientes**: Recebe o nome, e-mail e telefone dos clientes e realiza o cadastro.
- **Validação de e-mail**: O e-mail precisa ser válido, contendo "@" e um domínio ".com".
- **Formatação de telefone**: Remove todos os caracteres não numéricos do telefone.
- **Armazenamento**: Armazena os clientes cadastrados em um dicionário, onde o e-mail é usado como chave.

## Tecnologias Utilizadas

- **Python 3**: Linguagem utilizada para desenvolver o sistema.

## Como Utilizar

1. Execute o programa no terminal.
2. Insira as informações solicitadas (nome, e-mail e telefone) para cadastrar um novo cliente.
3. Caso queira parar o processo de cadastro, digite `"sair"` quando solicitado a inserir o nome.
4. Os clientes cadastrados serão exibidos ao final da execução do programa.

### Exemplo de Uso

```bash
Iniciando cadastro de clientes

Cadastro de nº 1
Por favor, digite o nome do cliente: (ou "sair" para encerrar): Pedro Alvaro
Por favor, digite o e-mail do contato: pedro.alvaro@gmail.com
Por favor, digite o telefone: (21) 99876-5432

Cadastro de nº 2
Por favor, digite o nome do cliente: (ou "sair" para encerrar): sair

Clientes cadastrados:
E-mail: pedro.alvaro@email.com
Nome: Pedro Alvaro
Telefone: 21998765432
