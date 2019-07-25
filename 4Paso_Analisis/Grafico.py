# -*- coding: utf-8 -*-
import argparse
import json
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
matplotlib.use('qt4agg')

if __name__ == '__main__':

	filename = "miStream.json"
	timeX = "hour"
	
	times_list = {}
	f = open(filename, 'r')
	for line in f:
		try:
			t = json.loads(line)
		except:
			continue
		try:
			tweet_time = datetime.strptime(t['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
		except:
			continue
		if timeX == 'minute':
			tweet_time = datetime.strftime(tweet_time, '%Y/%m/%d %H:%M')
			times_list[tweet_time] = 1 + times_list.get(tweet_time,0)
		if timeX == 'hour':
			tweet_time = datetime.strftime(tweet_time, '%Y/%m/%d %H')
			times_list[tweet_time] = 1 + times_list.get(tweet_time,0)
		if timeX == 'day':
			tweet_time = datetime.strftime(tweet_time, '%Y/%m/%d')
			times_list[tweet_time] = 1 + times_list.get(tweet_time,0)

	times = times_list.items()
	times.sort()
	
	xar = []
	yar = []
	
	for ht,abb in times:
		salidax = ht.split(' ')
		print "fecha: "+str(salidax[0])+" Hora: "+str(salidax[1])+ " Numero: " + str(abb)
		xar.append(int(salidax[1]))
		yar.append(int(abb))

	xar.sort()
	yar.sort()
	
	print xar
	print '\n\n\n\n'+str(yar)
	
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)
	ax1.clear()
	ax1.set_title("Tweet frecuenias")
	ax1.plot(xar,yar)
	ani = animation.FuncAnimation(fig, 0, interval=1000)
	plt.show()

