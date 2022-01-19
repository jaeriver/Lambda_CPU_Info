import subprocess
import json

def lambda_handler(event, context):
    command = ["cat", "/proc/cpuinfo"]
    output = subprocess.check_output(command)
    output = output.decode('ascii')
    print(output)
    
    return output
