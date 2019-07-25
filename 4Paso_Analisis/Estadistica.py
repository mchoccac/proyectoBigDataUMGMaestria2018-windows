# -*- coding: utf-8 -*-
import json
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

if __name__ == '__main__':

	filename = "miStream.json"
	timeX = "hour"
	
	times_list = {}
	
	f = open(filename, 'r')
	for line in f:
		try:
			t = json.loads(line)
			#print t
		except:
			continue
		try:
			tweet_timeX = datetime.strptime(t['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
		except:
			continue
		if timeX == 'minute':
			tweet_timeX = datetime.strftime(tweet_timeX, '%Y/%m/%d %H:%M')
			times_list[tweet_timeX] = 1 + times_list.get(tweet_timeX,0)
		if timeX == 'hour':
			tweet_timeX = datetime.strftime(tweet_timeX, '%Y/%m/%d %H')
			times_list[tweet_timeX] = 1 + times_list.get(tweet_timeX,0)
		if timeX == 'day':
			tweet_timeX = datetime.strftime(tweet_timeX, '%Y/%m/%d')
			times_list[tweet_timeX] = 1 + times_list.get(tweet_timeX,0)

	timesXY = times_list.items()
	timesXY.sort()
	
	xar = []
	yar = []
	
	for ht,abb in timesXY:
		salidax = ht.split(' ')
		print "fecha: "+str(salidax[0])+" Hora: "+str(salidax[1])+ " Numero: " + str(abb)
		xar.append(int(salidax[1]))
		yar.append(int(abb))

	xar.sort()
	yar.sort()
	
	print "\n\nDescribe x:\n"
	sx = pd.Series(xar)
	print sx.describe(include='all')
	print "\n\nDescribe y:\n"
	sy = pd.Series(yar)
	print sy.describe(include='all')
