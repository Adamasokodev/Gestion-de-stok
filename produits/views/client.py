from django.shortcuts import redirect, render
from produits.forms.client import ClientForm


def index(request):
    return render(request, 'pages/dashboard.html')

def create_client(request):
    if request.method == 'POST':
        client = ClientForm(request.POST)
        if client.is_valid():
            client.save()
            return redirect('list_client')
    else:
        client = ClientForm()
        return render(request, 'client/list_form.html')