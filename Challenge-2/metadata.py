import sys
import json
import requests

url = "http://10.0.0.4/metadata/instance/compute"
headers = {'metadata': 'true'}
params = (('api-version', '2021-08-25'),)
r = requests.get(url, headers=headers, params=params)

# Convert dict to json
out = json.dumps(r.json())
js = json.loads(out)

# Check if an argument is passed to the script
if len(sys.argv) > 1:
    arg = str(sys.argv[1])
    print(arg)
    if arg in js:
        print(js[arg])
    else:
        print("not found!")
# No argument passed, print the entire json
else:
    print(js)
