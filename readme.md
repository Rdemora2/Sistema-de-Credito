# Sistema de crédito

## Sobre o projeto
Desenvolvimento de uma interface web onde pessoas possam solicitar propostas de crédito.
A mesma passa por uma avaliação automatizada através de uma API de Análise de Crédito(https://loan-processor.digitalsys.com.br/swagger/index.html), caso a API retorne o status de não aprovado, a proposta é negada automaticamente, caso seja aprovada, é disponibilizada para avaliação humana.

## Layout web
![image](https://github.com/Rdemora2/Sistema-de-Credito/assets/103211332/9c15f102-c590-4839-8fbf-12b6e98382a2)

# Tecnologias utilizadas
## Back end
- Python
- Django
- Django rest framework
- Celery
- Redis

## Front end
- Javascript
- Vue.js

## Container
- Docker

# Como executar o projeto
Pré-requisitos: Docker

```bash
# clonar repositório
git clone https://github.com/Rdemora2/Portifolio.git

# buildar os containers docker
docker compose build

# subir os containers
docker compose up

# criar superuser do django admin
abra um terminal na raiz do projeto
docker exec -ti django_backend bash
python manage.py createsuperuser
preencha os campos e crie o super usuário com permissões administrativas

# acessar as respectivas urls
Frontend: http://localhost:8080/
backend: http://localhost:8000/

```

# Urls importantes do backend
 - Django admin: http://localhost:8000/admin/
 - Api para consulta formulários preenchidos: http://localhost:8000/api/credit-forms/
 - Endpoint de registro de novos formularios: http://localhost:8000/api/sis_credito/


# Portas utilizadas
- Backend: 8000
- Frontend: 8080
- PostgreSQL: 5432
- Redis: 6379

# Autor

Roberto de Moraes

https://www.linkedin.com/in/robertomoraeszarzur/
