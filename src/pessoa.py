import requests


class Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get(
            'https://chat.openai.com/c/c332e185-2ea3-4318-b93a-5d8f71706b06'
        )

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'

        self.dados_obtidos = False
        return 'Erro inesperado'
