from cryptography.fernet import Fernet
import os

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

def encontrar_arquivos(diretorio):
    lista_arquivos = []
    for raiz, dirs, files in os.walk(diretorio):
        for nome_arquivo in files:
            caminho_arquivo = os.path.join(raiz, nome_arquivo)
            if nome_arquivo != "ransoware.py" and not caminho_arquivo.endswith(".key"):
                lista_arquivos.append(caminho_arquivo)
    return lista_arquivos

def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print("Arquivos descriptografados com sucesso!")

if __name__ == "__main__":
    main()