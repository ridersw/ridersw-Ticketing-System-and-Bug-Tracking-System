from django.db import models

# Create your models here.

class tickets(models.Model):

	status_choices = (('Open', 'Open'), ('In Progress', 'In Progress'), ('Pending','Pending'), ('On Hold', 'On Hold'),('Closed', 'Closed'))

	assignment_group_choices = (('HelpDesk', 'HelpDesk'), ('ITSecAdmin', 'ITSecAdmin'), ('Operations','Operations'), ('Network', 'Network'),('Infrastructure', 'Infrastructure'))

	ticket_id 			= models.PositiveIntegerField(primary_key = True)
	#ticket_id 			= models.PositiveIntegerField()
	title 				= models.CharField(max_length = 100)
	summary				= models.TextField()
	assigned_engineer	= models.CharField(max_length = 100, default = "Shashi")
	focused				= models.BooleanField(default=False)
	status				= models.CharField(max_length = 20, choices = status_choices, default = 'Open')
	assignment_group	= models.CharField(max_length = 20, choices = assignment_group_choices, default = 'HelpDesk')
	submitted_by		= models.CharField(max_length = 100, default='Guest')
	#comments			= models.CharField(max_length = 2000, default = "")