from torrequest import TorRequest
from datetime import datetime
import sys
from urllib.request import urlopen
from json import load
import pandas as pd
import time


URL = sys.argv[0]

with TorRequest() as tr:
    response = tr.get(URL)

    response = tr.get('http://ipecho.net/plain')
    print('IP: ' + response.text)  # not your IP address
    print('Adding 1 correctly...')  # not your IP address
