import subprocess
import json

lambda_handler(event, context):
  output = subprocess.check_output(["cat", "/proc/cpuinfo"], shell=True, encoding='utf-8')
  print(output)
  return output
