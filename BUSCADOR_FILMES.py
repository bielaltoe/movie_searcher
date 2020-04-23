import requests #biblioteca para fazer requests
import json  #a resposta do programa vem em json, utilizo a biblioteca para mexer.

req = None
def requisicao(titulo, key):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=' + key)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('ERRO NA CONEXAO')
        return None

def printar_detalhes(filme):
    print('\nTitulo:', filme['Title'],)
    print('Ano:', filme['Year'])
    print('Sinopse:', filme['Plot'])
    print('Nota:', filme['imdbRating'])
    print('Atores:', filme['Actors'],)
    print('Diretores:', filme['Director'],)
    print('Escrito por:', filme['Writer'])
    print('Prêmios:', filme['Awards'])
    print('Tamanho:', filme['Runtime'])
    print('Gênero:', filme['Genre'])
    print('Data de Lançamento:', filme['Released'])
    print('Avaliações:', filme['Ratings'])
    print('Poster:', filme['Poster'])
    print('\n')

                                                   #api_key= 'e5cb41fc'
sair = False

while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('\nSaindo...')

    else:
        Key = input('Digite sua KEY ou digite SAIR para fechar: ')

        filme = requisicao(op, Key)

        if filme['Response'] == 'False':
            print('\nERRO\n> Filme não encontrado ou sua KEY é invalida.\n> Caso você não possua uma KEY acesse o site: https://bit.ly/2xW8D9V\n> Se esse não for o problema verifique o título do filme e tente novamente...\n')

        else:
            printar_detalhes(filme)











