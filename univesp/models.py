from django.db import models

# Criação da classe Aluno com os campos a serem
# inseridos no banco de dados.
class AlunoUnivesp(models.Model):
    nome=models.CharField(
        max_length=255,
        null=False,
        blank=False)
    sobrenome=models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    matricula = models.IntegerField(
        null=False,
        blank=False
    )

    atributos = models.Manager()

    def __str__(self):
        return f'{self.nome}, {self.sobrenome}, {self.matricula}'

