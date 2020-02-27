import urllib.request
import json
 
url = "http://api.open-notify.org/astros.json"
 
with urllib.request.urlopen(url) as f:  
    response_text = f.read().decode('utf-8')
    j = json.loads(response_text)
    print(j)
    




# How many people are in the space?


# Who are they?


# What craft(s) are they in?