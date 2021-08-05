from django.shortcuts import render

# Create your views here.
def homepage(request, *args, **kwargs):
	if not request.session.session_key:
		return render(request, "loginPage.html")
	return render(request, "main.html")