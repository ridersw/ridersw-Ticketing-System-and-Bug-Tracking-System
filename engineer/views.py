from django.shortcuts import render, redirect
from engineer.models import Engineer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def checkUserCreds(request):
	
	checkUsername = request.GET['uname']
	checkPassword = request.GET['psw']
	
	user = authenticate(request, username=checkUsername, password=checkPassword)
	# print(f'User: {user}')
	# print(f'checkUsername: {checkUsername}')
	# print(f'checkPassword: {checkPassword}')

	if user != None:
		login(request, user)
		return render(request, 'main.html')
	else:
		return render(request, 'loginPage.html', context = {'Error': 'Username or Password is Incorrect'})

def logout_view(request):
	if logout(request):
		print(f'Logout Successfully')
	return render(request, 'loginPage.html', context = {'Error': 'Logged Out Successfully'})
