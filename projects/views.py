from django.shortcuts import render

# Create your views here.
def project_homepage(request, *args, **kwargs):
	return render(request, "Projects_homepage.html", {})

