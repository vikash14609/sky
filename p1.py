import time
import urllib3
import sys
import socket
from time import sleep
import p2 as s
import p3 as g
import p4 as bb
import p5 as checkp
def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.mailsac.com", 80))
        return True
    except OSError:
        pass
    return False

p = is_connected()	
print (p)
a = s.hola()
jjbar = "|/-\\"
for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\r" + jjbar[i % len(jjbar)])
    sys.stdout.flush()
    #do something
b = g.sep()
c = s.dua()
mailsac = g.start()
d = checkp.check()


