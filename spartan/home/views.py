from passlib.hash import django_pbkdf2_sha256 as handler
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from lists.models import User
import re

def Index(request):
	if request.method == 'POST':
		try:
			u =  User.objects.get(email=request.POST['email'])
			if handler.verify(request.POST['mdp']+"5645a774-6c94-4521-8c0a-4fc23ed28ff1", u.mdp):
				request.session['user_id'] = u.id
				request.session['user_name'] = u.nom
				request.session['user_prenom'] = u.prenom
				return redirect('/lists/')
			else:
				return render(request, 'home/index.html')
		except ObjectDoesNotExist:
			pass
	return render(request, 'home/index.html')

def sign(request):
	if request.method == 'POST':
		if request.POST['nom'] != "" and request.POST['prenom'] != "" and request.POST['email'] != "" and request.POST['mdp'] != "":
			try:
				user = User.objects.get(email=request.POST['email'])
				return render(request, 'home/index.html')
			except ObjectDoesNotExist:
				verifemail = re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', request.POST['email'])
				if verifemail:
					i = User(nom=request.POST['nom'], prenom=request.POST['prenom'], email=request.POST['email'], mdp=handler.encrypt(request.POST['mdp']+"5645a774-6c94-4521-8c0a-4fc23ed28ff1"))
					i.save()
					request.session['user_id'] = i.id
					request.session['user_name'] = i.nom
					request.session['user_prenom'] = i.prenom
					return redirect('/lists/')
	return render(request, 'home/index.html')

def logout(request):
	try:
		del request.session['user_id']
		del request.session['user_name']
		del request.session['user_prenom']
	except KeyError:
		pass
	return redirect('/')

def login(request):
	return render(request, 'home/login.html')

def newsign(request):
	return render(request, 'home/sign.html')