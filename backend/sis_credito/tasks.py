import requests
from celery import shared_task
from .models import CreditForm

@shared_task
def send_credit_request(proposal_data):
    api_url = "https://loan-processor.digitalsys.com.br/api/v1/loan/"

    payload = {
        "document": proposal_data["cpf"],
        "name": proposal_data["full_name"]
    }

    try:
        response = requests.post(api_url, json=payload)
        response_data = response.json()

        # Atualize o campo credit_api_response no banco de dados
        credit_form = CreditForm.objects.get(id=proposal_data["credit_form_id"])
        credit_form.credit_api_response = response_data.get("approved", False)
        credit_form.save()

    except requests.RequestException as e:
        # Trate erros de requisição ou resposta da API
        print("Error:", e)