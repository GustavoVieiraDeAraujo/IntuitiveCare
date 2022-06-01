#Bibliotecas utilizadas
import os
from zipfile import ZipFile, ZIP_DEFLATED

#Função para descompactar um ZIP
def descompactarZip(arquivo, ondeDescompactar):
    with ZipFile(arquivo, 'r') as zip:
        zip.extractall(ondeDescompactar)

#Função para zipar um arquivo
def ziparArquivoDeUmaPasta(pasta, nomeDoArquivoDentroDaPasta, nomeDoArquivoZipado):
    listaArquivos = os.listdir(pasta)
    arquivoZipado = ZipFile(nomeDoArquivoZipado, "a", compression=ZIP_DEFLATED)
    arquivoZipado.write(os.path.join(pasta, listaArquivos[listaArquivos.index(
        nomeDoArquivoDentroDaPasta)]),  listaArquivos[listaArquivos.index(nomeDoArquivoDentroDaPasta)])
    arquivoZipado.close()
