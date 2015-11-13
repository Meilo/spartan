from django.shortcuts import render, redirect

def CreateList(request):
	return render(request, 'lists/index.html')

def Profil(request):
	if request.session.get('user_id', None) :
		return render(request, 'lists/profil.html')
	else:
		return redirect('/')
