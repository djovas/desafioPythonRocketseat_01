def cadastrarContato(contatos):
    print('\n\nCadastrar Contato')
    nome = input('Insira o nome: ')

    while True:
        try:
            telefone = int(input('Insira o telefone (Somente Núemros): '))
        except:
            ('Informações erradas! Utilize somente números!')
        else:
            break

    email = input('Insira o email: ')
    favorito = False

    dados = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'favorito': favorito
    }

    contatos.append(dados)

    return  contatos



def visualizarContatos(contatos):
    ('\n\nLista de Contatos')
    for x in range(len(contatos)):
        print(f'\nContato {x}')
        print(f'Nome: {contatos[x]["nome"]}')
        print(f'Telefone: {contatos[x]["telefone"]}')
        print(f'Email: {contatos[x]["email"]}')
        print(f'Favorito: {contatos[x]["favorito"]}')
    return



def editarContato(contatos):
    for x in range(len(contatos)):
        print(f'\nContato {x}')
        print(f'Nome: {contatos[x]["nome"]}')
        print(f'Telefone: {contatos[x]["telefone"]}')
        print(f'Email: {contatos[x]["email"]}')
        print(f'Favorito: {contatos[x]["favorito"]}')

    while True:
        try:
            id = int(input('\nInsira o id do contato que deseja editar: '))
        except:
            ('Informações erradas! Utilize somente números!')
        else:
            break


    
    while True:
        try:
            print('\nO que deseja alterar?')
            print('1 - Nome')
            print('2 - Telefone')
            print('3 - Email')
            print('0 - Sair')
            opcao = int(input('Insira a sua opção: '))
            if opcao == 1:
                nome = input('Insira o novo nome: ')
                contatos[id]['nome'] = nome
            elif opcao == 2:
                while True:
                    try:
                        telefone = int(input('Insira o novo telefone (Somente Núemros): '))
                    except:
                        ('Informações erradas! Utilize somente números!')
                    else:
                        contatos[id]['telefone'] = telefone
                        break
            elif opcao == 3:
                email = input('Insira o novo email: ')
                contatos[id]['email'] = email
            elif opcao == 0:
                return contatos
            else:
                break

        except:
            ('Informações erradas! Utilize somente números!')
        else:
            break
    
    return contatos



def setContatoFav(contatos):

    for x in range(len(contatos)):
        print(f'\nContato {x}')
        print(f'Nome: {contatos[x]["nome"]}')
        print(f'Telefone: {contatos[x]["telefone"]}')
        print(f'Email: {contatos[x]["email"]}')
        print(f'Favorito: {contatos[x]["favorito"]}')

    while True:
        try:
            id = int(input('Insira o id do contato que deseja marcar/desmarcar como favorito: '))
        except:
            ('Informações erradas! Utilize somente números!')
        else:
            break
    
    if contatos[id]['favorito'] == False:
        contatos[id]['favorito'] = True
    else:
        contatos[id]['favorito'] = False

    return contatos


def contatosFavoritos(contatos):
    for x in range(len(contatos)):
        if contatos[x]['favorito'] == True:
            print(f'\nContato {x}')
            print(f'Nome: {contatos[x]["nome"]}')
            print(f'Telefone: {contatos[x]["telefone"]}')
            print(f'Email: {contatos[x]["email"]}')
            print(f'Favorito: {contatos[x]["favorito"]}')
    return

def excluirContato(contatos):
    for x in range(len(contatos)):
        print(f'\nContato {x}')
        print(f'Nome: {contatos[x]["nome"]}')
        print(f'Telefone: {contatos[x]["telefone"]}')
        print(f'Email: {contatos[x]["email"]}')
        print(f'Favorito: {contatos[x]["favorito"]}')

    while True:
        try:
            id = int(input('Insira o id do contato que deseja excluir: '))
        except:
            ('Informações erradas! Utilize somente números!')
        else:
            break

    del contatos[id]
    return contatos


def menu():
    # Variavel onde serão armazenadas as informações dos contatos
    contatos = []

    while True:
        print('\nSeja bem vindo ao aplicativo de agenda!')
        print('Menu')
        print('1 - Cadastrar um Novo Contato')
        print('2 - Visualizar Contatos')
        print('3 - Editar um Contato')
        print('4 - Marcar/Desmarcar um Contato como Favorito')
        print('5 - Ver Lista dos Favoritos')
        print('6 - Apagar um Contato')
        print('0 - Sair')

        # Exceções para validar a opção selecionada
        try:
            opcao = int(input('\nDigite a opção: '))

            if opcao == 1:
                contatos = cadastrarContato(contatos)
            elif opcao == 2:
                visualizarContatos(contatos)
            elif opcao == 3:
                contatos = editarContato(contatos)
            elif opcao == 4:
                contatos = setContatoFav(contatos)
            elif opcao == 5:
                contatosFavoritos(contatos)
            elif opcao == 6:
                contatos = excluirContato(contatos)
            elif opcao == 0:
                break
            else: 
                print('Opção Inválida')

        except Exception as e:
            print('\nA Opção precisa ser um número!')
            print(e)

if __name__ == '__main__':
    menu()