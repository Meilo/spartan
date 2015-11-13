from django.db import models
from jsonfield import JSONField

class User(models.Model):
	nom = models.CharField(null=True, max_length=50)
	prenom = models.CharField(null=True, max_length=50)
	email = models.EmailField(null=True, max_length=100)
	mdp = models.CharField(null=True, max_length=100)
	lists = JSONField(null=True)

	def __str__(self):
		return self.nom

