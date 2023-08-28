from rest_framework import viewsets
from .models import LoanProposal
from .serializers import CreditForm

class CreditFormViewSet(viewsets.ModelViewSet):
    queryset = CreditForm.objects.all()
    serializer_class = CreditFormSerializer