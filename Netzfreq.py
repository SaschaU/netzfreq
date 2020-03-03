#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import requests
import time
import sys

Webseite = "https://www.netzfrequenz.info/json/act.json"
Quelle = "https://www.netzfrequenz.info"


if len(sys.argv[1:]) == 1:
	count = int(sys.argv[1])


elif len(sys.argv[1:]) >= 1:
	count = int(sys.argv[1])
	speed = int(sys.argv[2])

else:
	count = 5
	speed = 2

for A in range(1, count+1):
	time.sleep(speed)
	freq = requests.get(Webseite).text
	print str(A)+". Messung: "+freq+" Hz "

print "\033[33m"+"Es wurden "+str(count)+" Messungen im "+str(speed)+" Sekunden Abstand durchgeführt."+"\033[0m"
print "Quelle: "+str(Quelle)
