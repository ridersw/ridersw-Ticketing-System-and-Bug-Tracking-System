from django.shortcuts import render
from .models import tickets
from engineer.models import Engineer
from tickets.models import tickets
import random
from datetime import datetime
from tickets.mailUtility import getUpdate
import datetime
# Create your views here.

Operations = ['Shashi']
ITSecAdmin = ['Prithvi']
Network = ['Krishna']
DevTeam = ['Shubham']

def generateTicketID(request):

	obj = tickets.objects.all()

	ticket_array = []	
	for details in obj:
		ticket_array.append(int(details.ticket_id))
	
	return (max(ticket_array)+1)		

def view_tickets(request):
	if not request.session.session_key:
		return render(request, "loginPage.html")

	t1 = time.time()	
	obj = tickets.objects.all()
	print(f"Time Required: {time.time() - t1}" )
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
			temp.append(details.comments)



			ticket_data.append(temp)
			temp = []

	context = {

		#unique array

		'All_tickets_data'		: ticket_data,
		'current_message'		: "You are Viewing All Tickets"
	}
	print(f'length: {len(ticket_data)}')
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
			temp.append(details.comments)

			ticket_data.append(temp)
			temp = []

	context = {
		#unique array

		'All_tickets_data'		: ticket_data,
		'current_message'		: "You are Viewing Tickets assigned to your Group"
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
			temp.append(details.comments)

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
			temp.append(details.comments)

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
	
	t1 = datetime.datetime.now()	
	obj = tickets.objects.all()
	print(f"Time Required: {datetime.datetime.now() - t1}" )

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
		temp.append(details.comments)

		ticket_data.append(temp)
		temp = []

	context = {
		#unique array

		'All_tickets_data'		: ticket_data,
		'current_message'		: "You are Viewing All Tickets"
	}
	return render(request, "main.html", context)

def ticketDetails(request):

	if not request.session.session_key:
		return render(request, "loginPage.html")
	obj = tickets.objects.all()

	print(f"ticketID: {request.POST.get('ticketID', None)}")

	refTicketID = int(request.POST.get('ticketID', None))

	ticket_data = []
	temp = []

	for details in obj:
		#add data to unique array
		#print(f'Comparing {type(details.ticket_id)} and {type(refTicketID)}')
		if details.ticket_id == refTicketID:

			temp.append(details.ticket_id)
			temp.append(details.title)
			temp.append(details.summary)
			temp.append(details.assigned_engineer)
			temp.append(details.focused)
			temp.append(details.status)
			temp.append(details.assignment_group)
			temp.append(details.comments)

			ticket_data.append(temp)
			break

	

	context = {
		#unique array
		'message'				: 'Ticket Details',
		'All_tickets_data'		: temp
	}

	print(f'context: {context}')
	print(f'temp: {temp}')

	return render(request, 'ticketDetails.html', context)	

def createNewTicket(request):
	print("In Function createNewTicket")

	return render(request, 'createNewTicket.html')	
	#return render(request, 'ticketDetails.html')	

def createNewTicketOperation(request):

	#print(request.GET['createNewTicketButtonID'])	

	#print(f"if 'createNewTicketFormButton' in request.POST: {'createNewTicketFormButton' in request.POST}")

	print('Triggered Function createNewTicket')

	if not request.session.session_key:
		return render(request, "loginPage.html")



	if 'createNewTicketFormButton' in request.POST:	



		obj = tickets.objects.all()
		tempID = generateTicketID(request)
				
		ticket_id	= tempID
		ticket_title = request.POST['createNewTicketTitle']
		ticket_summary = request.POST['ticketSummary']
		assigned_engineer = 'Shashi'
		ticket_assignment_group  = request.POST['ticketAssignmentGroup']
		ticket_status = "Open"

		ticket_data = [ticket_id, ticket_title, ticket_summary, assigned_engineer, None,ticket_status, ticket_assignment_group]	

		print(ticket_data)

		msg = 'Ticket Created Successfully'

		tickets.objects.create(ticket_id = ticket_id, title = ticket_title, summary = ticket_summary, assigned_engineer = assigned_engineer, status = 'Open', assignment_group = 'Operations', submitted_by = request.user)	

		context = {
			#unique array

			'All_tickets_data'		: ticket_data,
			'message'			: msg
		}		
		
		

		return render(request, 'ticketDetails.html', context)



	elif 'updateTicketFormButton' in request.POST:

		ticket_id	= request.POST['ticketID']
		ticket_title = request.POST['title']
		ticket_summary = request.POST['summary']
		assigned_engineer = request.POST['assignedEngineer']
		status = request.POST['status']
		assignmentGroup = request.POST['assignmentGroup']

		comments = []
		comments.append(request.POST['comments'])

		addionalComments = request.POST['additionalComments']

		if addionalComments:

			try: 
				tempUser = str(request.user)	
				print(f'Updated by request.user :{tempUser}')

			except:
				tempUser = str(assigned_engineer)
				print(f'Updated by assignedEngineer :{tempUser}')	
				
			tempComment = []
			tempComment.append('Date: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
			tempComment.append('Comment: ' + addionalComments)

			if tempUser:
				tempComment.append('Engineer: ' + tempUser)

			comments.append(tempComment)

			addionalComments = ""


		ticket_data = [ticket_id, ticket_title, ticket_summary, assigned_engineer,"" ,status, assignmentGroup, comments]

		try:
			tickets.objects.filter(ticket_id = ticket_id).update(title = ticket_title, summary = ticket_summary, comments = comments)	

			context = {
			#unique array
				'All_tickets_data'		: ticket_data,
				'message'			: "Ticket Updated Successfully"
			}

		except:

			context = {
			#unique array
				'All_tickets_data'		: ticket_data,
				'message'			: "Ticket Update Operation Failed. Please Contact Admin"
			}
				

		return render(request, 'ticketDetails.html', context)

	elif "requestUpdate" in request.POST:

		obj = tickets.objects.all()

		ticket_id	= request.POST['ticketID']
		ticket_title = request.POST['title']
		ticket_summary = request.POST['summary']
		assigned_engineer = request.POST['assignedEngineer']
		status = request.POST['status']
		assignmentGroup = request.POST['assignmentGroup']
		comments = request.POST['comments']

		engineerDetails = Engineer.objects.get(name=assigned_engineer)
		engineer_email = engineerDetails.emailID

		#print(engineer_email)

		user_name = request.user

		#reqUp = getUpdate(ticket_ID, engineer_ID, engineer_email, assigned_engineer, user_name, ticket_title)
		reqUp = getUpdate(ticket_id, ticket_title, assigned_engineer, engineer_email, user_name)

		ticket_data = [ticket_id, ticket_title, ticket_summary, assigned_engineer,"" ,status, assignmentGroup, comments]

		if reqUp:

			context = {
				'All_tickets_data'		: ticket_data,
				'message'			: "Update Request Mail Sent Successfully"	
			}

			return render(request, 'ticketDetails.html', context)

		else:
			context = {
				'All_tickets_data'		: ticket_data,
				'message'			: "Update Requested Failed. Please Contact Admin"	
			}		

			return render(request, 'ticketDetails.html', context)

def UIDashboard(request):

	context = {
		
	}

	return render(request, 'UIDashboard.html', context) 				