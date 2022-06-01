#Bibliotecas utilizadas
import os
import tabula
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

#Descompactando "Anexos.zip" na pasta "temporario"
descompactarZip("Anexos.zip", "./temporario")

#Converter "Anexo I.pdf" em "convertido.csv"
tabula.convert_into("./temporario/Anexo I.pdf","./temporario/convertido.csv", output_format="csv", pages="3-200")