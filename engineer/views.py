from django.shortcuts import render, redirect
from engineer.models import Engineer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from email.message import EmailMessage
from datetime import datetime
import sys
from random import randint
import smtplib


# Create your views here.

def checkUserCreds(request):

	if "otp" in request.POST:	
		OTPfromForm = request.POST['otp']

		randomOTP = request.POST['randomOTPLabel']
		userAuthenticated = request.POST['userAuthenticated']

		if int(OTPfromForm) == int(randomOTP):# and userAuthenticated:
			return render(request, 'main.html')	
		else:
			logout(request)		
			return render(request, 'loginPage.html', context = {'Error': 'OTP Validation Unsuccessful'})

	elif "login" in request.POST:	
	
		checkUsername = request.POST['uname']
		checkPassword = request.POST['psw']
		
		user = authenticate(request, username=checkUsername, password=checkPassword)
		# print(f'User: {user}')
		# print(f'checkUsername: {checkUsername}')
		# print(f'checkPassword: {checkPassword}')

		if user != None:
			#login(request, user)
			randomOTP = sendOTPonMail(checkUsername)
			return render(request, 'MFAPage.html',  context = {'randomOTP': randomOTP})
		else:
			return render(request, 'loginPage.html', context = {'Error': 'Username or Password is Incorrect'})

def logout_view(request):
	if logout(request):
		print(f'Logout Successfully')
	return render(request, 'loginPage.html', context = {'Error': 'Logged Out Successfully'})

def sendOTPonMail(checkUsername):

	#checkUsername = request.POST['uname']
	print('Sending Mail Initiated')
	userInfo = User.objects.get(username=checkUsername)
	userEmail = userInfo.email 

	if userEmail:
		print('Got User Email')
	else:
		print('User Email not found')			

	randomOTP = randint(100000, 999999) 

	password = "LondonParis#1"

	fromEmail = "ticketingtoolDjango@gmail.com"

	messages = f"""Greetings {userInfo.first_name},

	Below is the OTP for login-

	{randomOTP}

	This is an automated email. Please do not reply to this email as this mailbox is not monitored.

	Best,
	Bee, Ticketing Tool """


	msg = EmailMessage()
	if msg:
		print('msg set successfully')
	else:
		print('msg set failed')		

	msg.set_content(messages)
	if msg:
		print('msg content set successfully')
	else:
		print('msg content set failed')	

	now = datetime.now()
	now = now.strftime("%d/%m/%Y %H:%M:%S")

	msg['Subject'] = f'[Ticketing Tool] OTP for Login Request at {now}'
	msg['From'] = fromEmail

	msg['To'] = userEmail
     
	try: 
		print('Trying to send mail')
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.login(fromEmail, password)
		print('Server Login Successfully')
		server.send_message(msg)
		print(f"email sent successfully")
		server.quit()
		return randomOTP
	except: 	
		print('Error Occurred in Server Login')
		print(f'Error Sending Email to {userEmail}')
		sys.exit()
		return False  	