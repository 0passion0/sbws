import requests
import json
import time
import os
u='https://github.com/'
u=requests.get(u)
print(u.text)