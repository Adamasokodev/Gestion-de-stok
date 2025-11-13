from django.db import models
from django.core.validators import RegexValidator


telephone_regex = RegexValidator(
    regex=r'^(2[0-9]{7}|3[0-9]{7}|4[0-9]{7}|6[0-9]{7}|7[0-9]{7})$', 
    message="Veillez entrez un numéro valide (8 chiffres)"
)

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=8, validators=[telephone_regex])

    def __str__(self):
        return self.nom
    