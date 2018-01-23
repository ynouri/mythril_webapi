from django.test import TestCase
from analysis.serializers import *

class TestSerializers(TestCase):

	def test_isvalid(self):
		request_data = {"submission_type": "bytecode", "bytecode": "0x5050"}
		serializer = AnalysisSerializer(data=request_data)
		self.assertTrue(serializer.is_valid())

