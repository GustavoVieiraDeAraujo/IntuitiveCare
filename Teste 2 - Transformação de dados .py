#Bibliotecas utilizadas
from zipfile import ZipFile, ZIP_DEFLATED

#Função para descompactar um ZIP
def descompactarZip(arquivo, ondeDescompactar):
    with ZipFile(arquivo, 'r') as zip:
        zip.extractall(ondeDescompactar)


