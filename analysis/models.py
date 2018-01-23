from django.db import models
import uuid
import celery.states



class Analysis(models.Model):

	BYTECODE = 'bytecode'
	TYPE_CHOICES = ((BYTECODE, 'bytecode'),)
	RESULT_CHOICES = [(str(state), str(state).title()) for state in celery.states.ALL_STATES]

	created = models.DateTimeField(auto_now_add=True)
	submission_type = models.CharField(choices=TYPE_CHOICES, max_length=100)
	bytecode = models.TextField()
	uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	result = models.CharField(choices=RESULT_CHOICES, max_length=100, blank=True)
	error = models.TextField()
	issues = models.TextField()

	class Meta:
		ordering = ('created',)