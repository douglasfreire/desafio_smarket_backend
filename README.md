# desafio_smarket_backend
Teste tecnico da smarket

##Tecnologia usada:
- Django 2.2
- djangorestframework 3.12.2
- python 3.9
- IDE pycharm
- Banco de dados sqlite3 (Nativo do Django)

## Rodando o projeto

Faça um clone do project
```
git clone git@github.com:matheusads/smarket_backend.git
```
Crie uma virtualenv
```
python -m venv venv
```

Ative a virtualenv(Linux)
```
source venv/bin/activate
```

Ative a virtualenv(Windows / PowerShell)
```
cd .\venv\Scripts\
.\activate
```

Instale as dependências
```
pip install -r requirements.txt
```

Rode o comando para criar as tabelas no banco de dados
```
python manage.py makemigrations
python manage.py migrate
```

Rode o comando para executar o servidor
```
python manage.py runserver
```

Quando o sistema estiver rodando acesse através da interface Django rest Framework
http://127.0.0.1:8000/api/ e existirá dois endpoints diponíveis

No endpoint ``` " /api/user/ " ``` poderá fazer as operações CRUD relacionados aos usuários
No endpoint ``` " /api/task/ " ``` poderá fazer as operações CRUD relacionados as tarefas

Para criar as tarefas é necessário criar um usuário antes.

Caso prefira pode utilizar um rest client para fazer as chamadas no endpoint.
Lembrando que é necessário adicionar o /api/ antes.

Endpoints disponíveis:
 ### Usuários
- [GET] http://127.0.0.1:8000/api/user
- [POST] http://127.0.0.1:8000/api/user/
- [DELETE] http://127.0.0.1:8000/api/user/ID
- [PUT] http://127.0.0.1:8000/api/user/ID
- [PATCH] http://127.0.0.1:8000/api/user/ID

no [POST] é necessário enviar na requisição um JSON:
```
{
	"name": "Nome do usuario aqui"
}
```

### Tarefas
- [GET] http://127.0.0.1:8000/api/task
- [POST] http://127.0.0.1:8000/api/task/
- [DELETE] http://127.0.0.1:8000/api/task/ID
- [PUT] http://127.0.0.1:8000/api/task/ID
- [PATCH] http://127.0.0.1:8000/api/task/ID

no [POST] é necessário enviar na requisição um JSON:
```
{
	"description":"",
	"status": "Criado",
	"user_id":1
}
```