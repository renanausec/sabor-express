import os

restaurantes = [{'nome':'Sushi Tema', 'categoria':'Japonesa', 'ativo':True},
                {'nome':'Luigi', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Minerão', 'categoria':'Mineira', 'ativo':True}]

def exibir_nome_do_programa():
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
          """)

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal... ')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)

def exibir_opcoes():
    
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair')

def finalizar_app():
    #no windows seria: os.system('cls') - puxa a biblioteca os importada no início e faz a limpeza da tela 
    exibir_subtitulo('Finalizando App... ')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria,
                            'ativo': False}

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | ativo')

    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado! ')

    voltar_ao_menu_principal()

def escolher_opcoes():

    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) #com o int() ele transforma o digitado em um inteiro, para funcionar o if, elif e else

        # print('Você escolheu a opção: ', opcao_escolhida)
        # print(type(opcao_escolhida))
        # print(type(1))

        # match opcao_escolhida:
        #     case 1:
        #         print('Cadastrar restaurante')
        #     case 2:
        #         print('Lista restaurante')
        #     case 3:
        #         print('Ativar restaurante')
        #     case 4:
        #         finalizar_app()
        #     case _:
        #         print("Opção inválida")

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()