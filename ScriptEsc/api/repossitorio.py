import requests as req


#llamada ala api
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept':'application/vnd.github.v3+json'}
request = req.get(url, headers=headers)
print(f'status code: {request.status_code}')

#guardar respuesta en una variable
response_dic = request.json()

#prosesando resultado
print(response_dic.keys())

#exportar la inf. sobre los repositorios
print(f"total de repositorios : {response_dic['total_count']}")
repo_dicts = response_dic['items']
print(f"repositorios retornados: {len(repo_dicts)}") 

#examinar el primer repositorio
repo_dict = repo_dicts[0]
print(f"\n keys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)