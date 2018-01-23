from django.test import TestCase
from analysis.tasks import myth_task
import time

class TestCelery(TestCase):
	
	# Creates a simple dummy myth task, wait 1s and check for success
	# TODO: might not work if the testing queue is full?
	def test_send_task(self):
		args = ["0x5050"]
		uuid_str = '12345678-1234-5678-1234-567812345678'
		task = myth_task.apply_async(args, task_id=uuid_str)
		time.sleep(2)
		self.assertEqual(task.status, 'SUCCESS')

	# Gets the Celery task created under test_send_task and check that the myth execution succeeded
	def test_get_task_result(self):
		uuid_str = '12345678-1234-5678-1234-567812345678'
		result = myth_task.AsyncResult(uuid_str).result
		error = result['stderr']
		issues = result['stdout']
		no_issues_expected = 'The analysis was completed successfully. No issues were detected.\n'
		self.assertEqual(issues, no_issues_expected)

