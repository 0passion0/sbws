import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
import urllib
import time
import image
import csv
u='https://www.hhi7.com/play/119882-0-0.html'
u=requests.get(u)

print(u.text)


