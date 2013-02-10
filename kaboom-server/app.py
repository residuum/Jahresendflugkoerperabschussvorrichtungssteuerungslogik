#!/usr/bin/env python

import RPi.GPIO as GPIO
import web
from time import sleep
        
urls = (
	'/(.*)', 'index',
)

render = web.template.render('templates/')

class index:        
	def GET(self, page):
		if page == '':
			return render.index()

	def POST(self, page):
		if page == 'shoot':
			post_params = web.input()
			pins = [7, 11, 13, 15, 19]
			pin = int(post_params.pin)
			time = int(post_params.time)
			if pin in pins and time < 15:
				GPIO.setmode(GPIO.BOARD)
				GPIO.setup(pin, GPIO.OUT)
				GPIO.output(pin, True)
				sleep(time)
				GPIO.output(pin, False)
				return "pin {0} time {1}".format(pin, time)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
