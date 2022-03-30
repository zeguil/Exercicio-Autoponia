# Exercicio Autoponia 🌱

Uma API REST para gerenciamento de plantas e regadores feita com django rest framework.

A API possui endpoints para realizar um CRUD de plantas, regadores e usuários.


### 🎲 Rodando a API

```bash
# Clone este repositório
$ git clone <https://github.com/zeguil/Exercicio-Autoponia>

# Acesse a pasta do projeto no terminal/cmd
$ cd Exercicio-Autoponia

# Instale o virtualenv
$ pip install virtualenv 

# Crie um ambiente virtual
$ virtualenv venv (windows)

# Acesse o ambiente virtual
$ venv/Scripts/activate (windows)

#  Instale as bibliotecas necessarias 
$ pip install -r requirements.txt

# Execute a aplicação em modo de desenvolvimento
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://localhost:8000/api/v1/>
# Para ver a documentação e todos os endpoints disponiveis - acesse <http://localhost:8000/api/v1/swagger/>

```
<br>

### 🙍‍♂️ Criando um usuário

```sh
acesse - <http://localhost:8000/api/v1/usuarios/>
```

```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "autoponia", "password": "hello123", "password_confirm": "hello123", "is_staff": true, "is_superuser": true}' 

```

### 🔑 Autenticação
* ####  Para receber o token de acesso:
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "autoponia", "password": "hello123"}' \
  http://localhost:8000/api/v1/token/

...
{
  "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
  "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
```
* #### Você deve usar o token de acesso retornado no Header da requisição para comprovar a autenticação:  
(caso o usuário não esteja autenticado, só podera usar o método GET)
```
curl \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
```

* ####  Quando o token de acesso expirar, você deve realizar o refresh passando o antigo token no corpo da requisição para obter um novo token de acesso:
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"}' \
  http://localhost:8000/api/v1/token/refresh/

...
{"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w"}
```  

### ☀️ Informação sobre o clima
#### Você pode descobrir informações como temperatura e umidade de uma planta passando o id dela.
####Exemplo:
```
http://example.com/api/v1/plamtas/{id}/clima
```  

### 🔎 Buscas

#### Tambem é possivel fazer buscas através da url, digitando campo e valor:
####Exemplo:
```
http://example.com/api/v1/usuarios/?username=autoponia
```  

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [OpenWeather](https://openweathermap.org/)


<br>

**By: José Guilherme Lins**