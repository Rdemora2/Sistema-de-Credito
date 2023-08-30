# Sistema de crédito
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

# Sobre o projeto
Desenvolvimento de uma interface web onde pessoas possam solicitar propostas de crédito.
A mesma passa por uma avaliação automatizada através de uma API de Análise de Crédito(https://loan-processor.digitalsys.com.br/swagger/index.html), caso a API retorne o status de não aprovado, a proposta é negada automaticamente, caso seja aprovada, é disponibilizada para avaliação humana.

## Layout web
> :construction: Em construção :construction:

# Tecnologias utilizadas
## Back end
- Python
- Django
- Django rest framework
- Django Celery

## Front end
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
```

# Autor

Roberto de Moraes

https://www.linkedin.com/in/robertomoraeszarzur/