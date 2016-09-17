import cherrypy
import os
from cherrypy import request
from jinja2 import Environment, FileSystemLoader
import RPi.GPIO as GPIO
import time

env = Environment(loader=FileSystemLoader('templates'))

pins = [[11,'off'], [12,'off'], [13,'off'], [15,'off'], [16,'off'], [18,'off'], [22,'off'], [7, 'off']]
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for pin in pins:
    GPIO.setup(pin[0], GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(pin[0], GPIO.HIGH) # Set LedPin high(+3.3V) to off led

class MainPage(object):
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()
    def switchlight(self, lightNum):
        toggle_led = int(lightNum)
        if pins[toggle_led -1][1] == 'on':
            GPIO.output(pins[toggle_led -1][0], GPIO.HIGH)
            pins[toggle_led -1][1] = 'off'
        elif pins[toggle_led -1][1] == 'off':
            GPIO.output(pins[toggle_led -1][0], GPIO.LOW)
            pins[toggle_led -1][1] = 'on' 
    
    index.exposed = True
    switchlight.exposed = True

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(MainPage(), '/', conf)
