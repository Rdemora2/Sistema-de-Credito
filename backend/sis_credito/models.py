from django.db import models

class CreditForm(models.Model):
    full_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    address = models.TextField()
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    credit_api_response = models.JSONField(null=False, blank=False)
