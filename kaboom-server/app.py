#!/usr/bin/env python

import RPi.GPIO as GPIO
import web
import json
from time import sleep

class pin:
	def __init__(self, no, status):
		self.no = no
		self.status = status
#	def __repr__(self):
#		return json.dumps(self.__dict__)
        
def jdefault(o):
	return o.__dict__

urls = (
	'/(.*)', 'index',
)

render = web.template.render('templates/')

class index:
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		self.pins = [13, 11, 7, 15, 19]
		for pin in self.pins:
			GPIO.setup(pin, GPIO.OUT)
	
	def GET(self, page):
		if page == '':
			return render.index()
		if page == 'status':
			stati = []
			for pinNo in self.pins:
				GPIO.setup(pinNo, GPIO.IN)
				status = pin(pinNo, GPIO.input(pinNo))
				stati.append(status)
			web.header('Content-Type', 'application/json')
			return json.dumps(stati, default=jdefault)

	def POST(self, page):
		if page == 'shoot':
			params = json.loads(web.data())
			pin = int(params['pin'])
			time = int(params['time'])
			if pin in self.pins and time < 25:
				GPIO.setup(pin, GPIO.OUT)
				GPIO.output(pin, True)
				sleep(time)
				GPIO.setup(pin, GPIO.OUT)
				GPIO.output(pin, False)
				web.header('Content-Type', 'application/json')
				return json.dumps(params);
			return ''

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
