saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
depo = 0

def opcoes():
    menu = input('Digite a opção:\n [d] Depositar\n [s] Sacar\n [e] Extrato\n [q] Sair\n')
    return menu

def deposito(valor):
    global saldo
    global depo
    if valor > 0:
        saldo += valor
        depo += 1
        print(f'Valor do depósito R${valor:.2f}')
        return saldo

def sacar(valor):
    global saldo
    global numero_saques
    if saldo > 0 and numero_saques < LIMITE_SAQUES and valor <= limite:
        saldo -= valor
        numero_saques += 1
        print(f'Valor do saque R${valor:.2f}')
    else:
        print('Não é possível fazer o saque. Não há valor disponível ou excedeu o limite de saques.')

opcao = opcoes()

while True:
    if opcao == 'd':
        valor = float(input('Digite o valor para depositar: '))
        deposito(valor)
    elif opcao == 's':
        valor = float(input('Digite o valor para sacar: '))
        sacar(valor)
    elif opcao == 'e':
        print(f'O total de depósitos da conta foi {depo}')
        print(f'O total de saques da conta foi {numero_saques}')
        print(f'R${saldo:.2f}')
    elif opcao == 'q':
        print(f'O total de depósitos da conta foi {depo}')
        print(f'O total de saques da conta foi {numero_saques}')
        print(f'R${saldo:.2f}')
        break
    else:
        print('Opção inválida!')

    opcao = opcoes()
