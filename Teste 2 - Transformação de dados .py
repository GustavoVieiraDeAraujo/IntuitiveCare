#Bibliotecas utilizadas
import os
import csv
import shutil
import tabula
from zipfile import ZipFile, ZIP_DEFLATED

#Função para formatar linhas do arquivo CSV
def formatarLinha(linha):
    for i in linha:
        if "\n" in i:
            linha[linha.index(i)] = i.replace("\n", " ")
    return linha

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

#Gerando "Anexo I.csv" utilizando "convertido.csv"
with open("./temporario/convertido.csv", "r", encoding='utf-8') as convertido:
    with open("./temporario/Anexo I.csv", 'w', encoding='utf-8') as formatado:
        matriz_csv_file = csv.reader(convertido)
        csv.writer(formatado, delimiter=',').writerow(['PROCEDIMENTO', 'RN (alteração)', 'VIGÊNCIA', 'Seg. Odontológica',
                                                       'Seg. Ambulatorial', 'HCO', 'HSO', 'REF', 'PAC', 'DUT', 'SUBGRUPO', 'GRUPO', 'CAPÍTULO'])
        for linha in matriz_csv_file:
            if linha[0] == "PROCEDIMENTO":
                pass
            else:
                csv.writer(formatado, delimiter=',').writerow(
                    formatarLinha(linha))

#Zipando o arquivo "Anexo I.csv"
ziparArquivoDeUmaPasta("./temporario", "Anexo I.csv",
                       "Teste_Gustavo_Vieira_de_Araújo.zip")
                       
#Excluindo pasta "temporario"
shutil.rmtree("./temporario")