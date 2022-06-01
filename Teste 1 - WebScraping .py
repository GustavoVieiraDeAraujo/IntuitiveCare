# Bibliotecas utilizadas
import os
import requests
from requests.exceptions import HTTPError
from zipfile import ZipFile, ZIP_DEFLATED

# Função para baixar arquivo
def baixarArquivo(url, pastaOndeFicaSalvo):
    try:
        repostaServidor = requests.get(url)
        with open(pastaOndeFicaSalvo, "wb") as arquivo:
            arquivo.write(repostaServidor.content)
        repostaServidor.raise_for_status()
    except HTTPError as http_err:
        print(f'Ocorreu um erro HTTP: {http_err}')
        print(f"Download falhou.")
    except Exception as erro:
        print(f'Outro erro ocorreu: {erro}')
        print(f"Download falhou.")
    else:
        print(f"Download concluido com sucesso.")

# Função para Zipar Pasta
def ziparPasta(pasta, nomeArquivoZipado):
    listaArquivos = os.listdir(pasta)
    arquivoZipado = ZipFile(nomeArquivoZipado, "a", compression=ZIP_DEFLATED)
    for arquivo in listaArquivos:
        arquivoZipado.write(os.path.join(pasta, arquivo), arquivo)
    arquivoZipado.close()

# Variaveis para construção da URL
endereçoBase = "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/"
dicionarioEndereçosArquivos = {
    "Anexo I.pdf": "Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf",
    "Anexo I.xlsx": "Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.xlsx",
    "Anexo II.pdf": "Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf",
    "Anexo III.pdf": "Anexo_III_DC_2021_RN_465.2021.v2.pdf",
    "Anexo IV.pdf": "Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf",
}
