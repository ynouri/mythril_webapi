from django.db import models
import uuid


class Analysis(models.Model):

	BYTECODE = 'bytecode'
	QUEUED = 'Queued'
	IN_PROGRESS = 'In progress'
	FINISHED = 'Finished'
	ERROR = 'Error'

	TYPE_CHOICES = (
		(BYTECODE, 'bytecode'),
	)

	RESULT_CHOICES = (
		(QUEUED, 'Queued'),
		(IN_PROGRESS, 'In Progress'),
		(FINISHED, 'Finished'),
		(ERROR, 'Error')
	)

	created = models.DateTimeField(auto_now_add=True)
	submission_type = models.CharField(choices=TYPE_CHOICES, max_length=100)
	bytecode = models.TextField()
	uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	result = models.CharField(choices=RESULT_CHOICES, max_length=100, blank=True)
	error = models.TextField()
	issues = models.TextField()

	class Meta:
		ordering = ('created',)