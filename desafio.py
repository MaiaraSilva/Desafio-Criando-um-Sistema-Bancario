saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
depo = 0

while True:
    menu = input('Digite a opção:\n [d] Depositar\n [s] Sacar\n [e] Extrato\n [q] Sair\n')

    if menu == 'd':
        valor = float(input('Digite o valor de depósito: '))
        saldo += valor
        depo += 1
        print(f'Valor do depósito R${valor:.2f}')

    elif menu == 's':
        valor_saque = float(input('Digite o valor que deseja sacar: '))
        if saldo > 0 and numero_saques < LIMITE_SAQUES and valor_saque <= limite:
            saldo -= valor_saque
            numero_saques += 1
            print(f'Valor do saque R${saldo:.2f}')
        else:
            print('Não é possível fazer o saque. Não há valor disponível ou excedeu o limite de saques.')

    elif menu == 'e':
        print(f'O total de depósitos da conta foi {depo}')
        print(f'O total de saques da conta foi {numero_saques}')
        print(f'R${saldo:.2f}')

    elif menu == 'q':
        break

    else:
        print('Operação inválida, por favor, selecione novamente a operação desejada')
