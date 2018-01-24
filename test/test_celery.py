from django.test import TestCase
from analysis.tasks import myth_task
import time
from test.contracts import contracts

CALL_WITH_DYNAMIC_ADDRESS = "CALL with gas to dynamic address"
NO_ISSUES_DETECTED = "No issues were detected"

class TestCelery(TestCase):
	
	# Creates a simple dummy myth task, wait 1s and check for success
	# TODO: might not work if the testing queue is full?
	def test_send_task(self):
		args = ["0x5050"]
		uuid_str = '12345678-1234-5678-1234-567812345678'
		task = myth_task.apply_async(args, task_id=uuid_str)
		time.sleep(5)
		self.assertEqual(task.status, 'SUCCESS')

	# Gets the Celery task created under test_send_task and check that the myth execution succeeded
	def test_get_task_result(self):
		uuid_str = '12345678-1234-5678-1234-567812345678'
		result = myth_task.AsyncResult(uuid_str).result
		error = result['stderr']
		issues = result['stdout']
		self.assertIn(NO_ISSUES_DETECTED, issues)

	# Smart contract bytecode which returns issues
	def test_bytecode_with_issues(self):
		args = [contracts[9]]
		task = myth_task.apply_async(args)
		time.sleep(5)
		self.assertIn(CALL_WITH_DYNAMIC_ADDRESS, task.result['stdout'])


