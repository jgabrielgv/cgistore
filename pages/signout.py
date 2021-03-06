#!/usr/bin/python3
"""This script shows the logout an user from his current session"""
import time
import os
import sys

__SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
__SCRIPT_DIR = os.path.normpath(os.path.join(__SCRIPT_DIR, '..'))
if not __SCRIPT_DIR in sys.path:
    sys.path.append(__SCRIPT_DIR)

from data.dao import Connection
from utils import config, helpers, session

sess = session.Session(expires='Thu, 01 Jan 1970 00:00:00 GMT', cookie_path='/')
#lastvisit = sess.data.get('lastvisit')
#if lastvisit:
#    message = 'Welcome back. Your last visit was at ' + \
#        time.asctime(time.gmtime(float(lastvisit)))
#else:
#    message = 'New session'
# Save the current time in the session
#sess.data['lastvisit'] = repr(time.time())
#cookie_file = helpers.format_cookie_path(sess.cookie['sid'].value)
#os.remove(cookie_file)
sess.cookie['sid']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'

conn = Connection()
delete_cookie = conn.delete_user_history(sess.cookie['sid'].value)

for cookie in sess.cookie:
    sess.cookie[cookie]['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
#sess.cookie["sid"] = ''
#sess.close()
#sess.cookie.clear()
print("Location: signin.py")
print("""\
%s
Content-Type: text/plain\n
sess.cookie = %s
""" % (sess.cookie, sess.cookie))
sess.cookie.clear()
#print "Content-type: text/html\n\n"
