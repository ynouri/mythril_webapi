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
