
fila = []

while True:
    escolha = input('''
1: Marcar consulta
2: Avançar lista
3: Verificar lista
4: Sair
Digite o número: ''')

    if escolha == '1':
        nome = input('Digite o seu nome para marcar consulta: ')
        fila.append(nome)
    elif escolha == '2':
        fila.pop(0)
    elif escolha == '3':
        print('A situação da fila atual é: ')
        for index, nome in enumerate(fila, start=1):
            print(f'{index}. {nome}')
    elif escolha == '4':
        print('Saindo do aplicativo')
        break
    else:
        print('Número inválido!')





