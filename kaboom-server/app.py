#!/usr/bin/env python

# Copyright (c) 2012-2013 Thomas Mayer <thomas@residuum.org>
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
# THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import RPi.GPIO as GPIO
import web
import json
from time import sleep

class pin:
	def __init__(self, no, status):
		self.no = no
		self.status = status
        
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
