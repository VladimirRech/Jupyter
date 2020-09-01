from urllib.request import urlopen
import sys

def recuperar_palavras(url):
	with urlopen(url) as musica:
		palavras_musica = []
		for linha in musica:
			palavras_linha = linha.decode('utf-8').split()
			for palavra in palavras_linha:
				palavras_musica.append(palavra)

	return palavras_musica

def imprimir_palavras(palavras_musica):
    for palavra in palavras_musica:
        print(palavra)

def main(url):
    palavras = recuperar_palavras(url)
    imprimir_palavras(palavras)

if __name__ == '__main__':
    main(sys.argv[1])
    
