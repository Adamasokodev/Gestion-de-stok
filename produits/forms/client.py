from django.forms import ModelForm
from produits.models.client import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client()
        fields = ('nom', 'email', 'telephone', 'adresse') 