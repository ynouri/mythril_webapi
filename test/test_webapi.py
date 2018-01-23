from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from analysis.models import Analysis
import time
from test.contracts import contracts

class TestWebApi(APITestCase):


	def test_1_bytecode_submission(self):
		"""
		Submits a smart contract bytcode
		"""		
		url = reverse('bytecode_submission')
		data = {'submission_type': 'bytecode', 'bytecode': contracts[9]}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Analysis.objects.count(), 1)


	def test_2_status(self):
		"""
		Checks the analysis status
		"""	

		# Submits new bytecode
		url = reverse('bytecode_submission')
		data = {'submission_type': 'bytecode', 'bytecode': contracts[9]}
		response = self.client.post(url, data, format='json')
		uuid = response.data['uuid']
		time.sleep(1)

		# Checks status
		url = reverse('status', args=[uuid])
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_3_report(self):
		"""
		Checks the analysis security issues report
		"""	

		# Submits new bytecode
		url = reverse('bytecode_submission')
		data = {'submission_type': 'bytecode', 'bytecode': contracts[9]}
		response = self.client.post(url, data, format='json')
		uuid = response.data['uuid']
		time.sleep(5)

		# Checks status
		url = reverse('report', args=[uuid])
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)