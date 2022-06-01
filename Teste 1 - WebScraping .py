# Bibliotecas utilizadas
import requests
from requests.exceptions import HTTPError

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

