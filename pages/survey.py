#!/usr/bin/python
"""This script shows the suggerents for no register users"""

import sys, os
import urllib

__SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
__SCRIPT_DIR = os.path.normpath(os.path.join(__SCRIPT_DIR, '..'))
if not __SCRIPT_DIR in sys.path:
    sys.path.append(__SCRIPT_DIR)

from utils import constants
from utils.helpers import pagetemplate, valiadtionMessage, ucgiprint, loadhtml, FormParser

body = loadhtml('survey.html')
wholepage = pagetemplate.replace('**title**', 'Sugerencias').replace('**css**', constants.DEFAULT_CSS).replace('**body**', body).replace('#action', 'signin.py')
ucgiprint(wholepage)
#sURL = os.path.realpath('.')
#print sURL
#url = os.environ["REQUEST_URI"] 
#final_url= "http://127.0.0.1/\x7Emcanales/cgi-bin/survey.py"
#print final_url
#final_url= urllib.urlencode("http://127.0.0.1/~mcanales/cgi-bin/survey.py")
#print final_url