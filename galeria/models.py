from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
# Essa classe representa uma tabela no banco de dados
class Fotografia(models.Model):
    #null = nao pode ser um campo vazio, blank=string vazia
    OPCOES_CATEGORIA = [
        ("CALCA", "Calça"),
        ("CASACO", "Casacos"), 
        ("CAMISA", "Camisas"), 
        ("TENIS", "Tênis"),
        ("CONJUNTO", "Conjuntos")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=100.00, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default='')
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    publicada = models.BooleanField(default=False)
    data_produto = models.DateTimeField(default=datetime.now, blank=False)
    usuarios = models.ForeignKey(
        to = User,
        on_delete= models.SET_NULL,
        null= True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        return self.nome