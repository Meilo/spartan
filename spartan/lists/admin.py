from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ('nom', 'prenom', 'email')
	readonly_fields = ('mdp',)
	fieldsets = [('Utilisateur', {'fields':['nom', 'prenom', 'email', 'mdp']}),
	('Json des lists', {'fields':['lists']}),]

admin.site.register(User, UserAdmin)