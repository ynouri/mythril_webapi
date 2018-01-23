from celery import shared_task
import os
import subprocess

@shared_task
def myth_task(bytecode):
	mythril_dir = "/Users/ynouri/Dropbox/Projects/Topcoder-Mythril/mythril/"
	args = ['myth', '-x', '-c', bytecode]
	p = subprocess.Popen(args, cwd=mythril_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout = p.stdout.read().decode('utf-8')
	stderr = p.stderr.read().decode('utf-8')
	task_result = {'stdout': stdout, 'stderr': stderr}
	return task_result