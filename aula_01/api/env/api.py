import requests

#1 Qual endereço que iremos requisitar
url = 'https://viacep.com.br/ws/{cep}/json/'

#2 informar um cep
cep = '27273010' #ou input

#3 fazer requisição https
response = requests.get(url)
response.raise_for_status()

print(response.status_code)
print(response)

        
