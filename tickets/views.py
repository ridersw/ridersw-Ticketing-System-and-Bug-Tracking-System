from django.shortcuts import render
from .models import tickets
from engineer.models import Engineer
# Create your views here.


def view_tickets(request):
	if not request.session.session_key:
		return render(request, "loginPage.html")
	obj = tickets.objects.all()

	#unique Array
	ticket_data = []
	temp = []

	for details in obj:
		if details.focused == True:
		#add data to unique array
			temp.append(details.ticket_id)
			temp.append(details.title)
			temp.append(details.summary)
			temp.append(details.assigned_engineer)
			temp.append(details.focused)
			temp.append(details.status)
			temp.append(details.assignment_group)


			ticket_data.append(temp)
			temp = []

	context = {

		#unique array

		'All_tickets_data'		: ticket_data
	}
	return render(request, "main.html", context)
	
def assignedToMyGroup(request):
	if not request.session.session_key:
		return render(request, "loginPage.html")
	#context = {}
	eng_obj = Engineer.objects.get(name=request.user)
	myGroup = eng_obj.engineer_group

	obj = tickets.objects.all()

	#unique Array

	ticket_data = []

	temp = []
	for details in obj:
		if details.assignment_group == myGroup:
			#add data to unique array

			temp.append(details.ticket_id)
			temp.append(details.title)
			temp.append(details.summary)
			temp.append(details.assigned_engineer)
			temp.append(details.focused)
			temp.append(details.status)
			temp.append(details.assignment_group)

			ticket_data.append(temp)
			temp = []

	context = {
		#unique array

		'All_tickets_data'		: ticket_data
	}
	return render(request, "main.html", context)


def assignedToMe(request):
	if not request.session.session_key:
		return render(request, "loginPage.html")
	myName = str(request.user)

	obj = tickets.objects.all()

	#unique Array

	ticket_data = []
	temp = []

	for details in obj:
		if details.assigned_engineer == myName:
			
			#add data to unique array

			temp.append(details.ticket_id)
			temp.append(details.title)
			temp.append(details.summary)
			temp.append(details.assigned_engineer)
			temp.append(details.focused)
			temp.append(details.status)
			temp.append(details.assignment_group)

			ticket_data.append(temp)
			temp = []

	context = {
		#unique array

		'All_tickets_data'		: ticket_data
	}
	return render(request, "main.html", context)


def submittedByMe(request):
	if not request.session.session_key:
		return render(request, "loginPage.html")
	myName = str(request.user)
	obj = tickets.objects.all()

	#unique Array
	ticket_data = []
	temp = []

	for details in obj:

		if str(details.submitted_by) == myName:
			#add data to unique array
			temp.append(details.ticket_id)
			temp.append(details.title)
			temp.append(details.summary)
			temp.append(details.assigned_engineer)
			temp.append(details.focused)
			temp.append(details.status)
			temp.append(details.assignment_group)

			ticket_data.append(temp)
			temp = []

	context = {
		#unique array

		'All_tickets_data'		: ticket_data
	}
	return render(request, "main.html", context)


def showTickets(request):
	if not request.session.session_key:
		return render(request, "loginPage.html")
	obj = tickets.objects.all()

	#unique Array

	ticket_data = []
	temp = []

	for details in obj:
		#add data to unique array

		temp.append(details.ticket_id)
		temp.append(details.title)
		temp.append(details.summary)
		temp.append(details.assigned_engineer)
		temp.append(details.focused)
		temp.append(details.status)
		temp.append(details.assignment_group)

		ticket_data.append(temp)
		temp = []

	context = {
		#unique array

		'All_tickets_data'		: ticket_data
	}
	return render(request, "main.html", context)