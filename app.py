import os

restaurantes = [{'nome' : 'ItaliaGo', 'categoria' : 'Italiano', 'ativo' : False},
                {'nome' : 'Arte Sushi', 'categoria' : 'Japonesa', 'ativo' : True},
                {'nome' : 'Comida Boa', 'categoria' : 'Caseira', 'ativo' : False}
                ]


def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    \n""")

def exibir_opcoes():
    print ('1 - Cadastrar Restaurante')
    print ('2 - Listar Restaurante')
    print ('3 - Ativar Restaurante')
    print ('4 - Sair\n')

def finalizar_app():
    os.system('cls')
    print("Encerrando programa\n")

def voltar_ao_menu_principal():
    input('\nDigite qualquer tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome}: ')
    dados_do_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome} foi cadastrado com sucesso')
    listar_restaurantes()
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Ativo'.ljust(20)}')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulo('Alternar Estado do Restaurantes')
    nome_restaurante = input('Qual restaurante deseja alterar estado?')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante['nome']} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {restaurante['nome']} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')

    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main ():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()