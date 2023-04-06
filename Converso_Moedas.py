from time import sleep

valor = 0

# Programa desenvolvido no dia 06/04/2023, valor das moedas podem ter sofrido alterações.
preço_dolar = 5.06 # Preço do Dolar
preço_libra = 6.30 # Preço da libra
preço_euro = 5.53 # Preço do euro

print('=' * 50)
print('CONVERSOR DE MOEDAS'.center(50))
print('=' * 50)

while True:
    valor = float(input('Informe o valor em R$(reais): R$ '))  # Converte o valor para float
    print('=' * 100)
    opcao = int(input('Informe para qual moeda deseja converter:\n'
                    '[1] DOLAR\n[2] EURO\n[3] LIBRA\nOpção desejada: ')) # Coleta a opção desejada pelo usuário
    print('=' * 100)
    if opcao == 1:
        calculo_dolar = valor * preço_dolar  # Faz o calculo do real para dolar
        print('Calculando...')
        sleep(1)
        print(f'A conversão de R${valor:.0f} para dolar é ${calculo_dolar:.0f}.') # Imprime na tela a conversão para dolar
    elif opcao == 2:
        calculo_euro = valor * preço_euro  # Faz o calculo do real para euro
        print('Calculando...')
        sleep(1)
        print(f'A conversão de R${valor:.0f} para euro é €{calculo_euro:.0f}.') # Imprime na tela a conversão para euro
    elif opcao == 3:
        calculo_libra = valor * preço_libra  # Faz o calculo do real para libra
        print('Calculando...')
        sleep(1)
        print(f'A conversão de R${valor:.0f} para libra é £{calculo_libra:.0f}.')  # Imprime na tela a conversão para libra
    elif opcao > 3 or opcao <= 0:
        print('Informe uma opção valida.')
    print('=' * 100)
    opcao2 = int(input('Deseja encerrar o programa? \n[1] SIM\n[2] NÃO\nOpção desejada: '))
    if opcao2 == 1:  # Recebe a opção desejada pelo usuário e se caso for 1 encerra o programa
        break
    print('=' * 100)
print('Encerrando...')
sleep(2)
print('Programa encerrado com sucesso. Obrigado e volte sempre!')