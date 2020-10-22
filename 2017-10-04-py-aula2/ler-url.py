# ler-url.py
# Lê documento de texto de uma url passada por parâmetro.

from urllib.request import urlopen
# Import library necessária para ler argumentos passados pela linha de comando
import sys

# Os métodos precisam ser definidos antes de serem invocados
# Este é o módulo "__main__"
def main():
    if len(sys.argv) == 2:
        url = sys.argv[1] # usa o segundo parâmetro,  o primeiro é o nome do script
        print('Usando argumento enviado pelo terminal como url.')
    else:
        url = 'http://dinomagri.com/data/aquarela.txt'
        print('Usando url fixa.')
        
    wr = read_words(url)
    print(wr)

def read_words(url_to_open):
    with urlopen(url_to_open) as music:
        words = []
        for lin  in music:
            aux = lin.decode('utf8').split()
            for word in aux:
                words.append(aux)

    return words


if __name__ == "__main__":
    print('Executando no modo script.')
    main()
    
else:
    print('Executando no modo iterativo.')
    read_words('http://dinomagri.com/data/aquarela.txt')
