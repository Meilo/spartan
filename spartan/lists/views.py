from django.shortcuts import render, redirect
from .models import User

def CreateList(request):
	return render(request, 'lists/index.html')

def Profil(request):
	if request.session.get('user_id', None) :
		OneUser = User.objects.get(id=request.session['user_id'])
		return render(request, 'lists/profil.html', {'OneUser':OneUser})
	else:
		return redirect('/')
