from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CreditForm
from .serializers import CreditFormSerializer
from .tasks import send_credit_request

class CreditFormViewSet(viewsets.ModelViewSet):
    queryset = CreditForm.objects.all()
    serializer_class = CreditFormSerializer

    @action(detail=True, methods=['post'])
    def submit_form(self, request, pk=None):
        credit_form = self.get_object()
        serializer = self.get_serializer(instance=credit_form, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        send_credit_request.apply_async(
            args=[{
                "credit_form_id": credit_form.id,
                "cpf": credit_form.cpf,
                "full_name": credit_form.full_name
            }],
            countdown=0
        )

        return Response(serializer.data)
