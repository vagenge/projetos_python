# variavel = cria, pega, atualiza, deleta

# arquivos = cria, pega, atualiza, deleta

# banco de dados = cria, pegar, atualiza, deleta (CRUD - CREATE, READ, UPDATE, DELETE)

# API = mandar, pega, atualiza, deleta (REST) [METODOS]


import json, requests


def buscar_cep():
    cep = input('DIgita o seu cep: ')

    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    conteudo = json.loads(response.content)

    print(conteudo['bairro'])



#acessei a API MOCK
response = requests.get('https://63481b46db76843976ba8874.mockapi.io/alunos')

status = response.status_code

conteudo = json.loads(response.content)

print(conteudo)


#deletar
resposta = requests.delete('https://63481b46db76843976ba8874.mockapi.io/alunos/2')

print(resposta.status_code)


dados = {
  "foto": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/656.jpg",
  "usuario": "elbulidur",
  "senha": "mynha",
  "nome": "Mrs. Walter Will",
  "turma": "turma 3",
  "media": 53,
  "situacao": "situacao 3",
  "ativo": False
 }

#Criar alunos
resposta = requests.post('https://63481b46db76843976ba8874.mockapi.io/alunos', data=dados)

print(resposta.status_code)


