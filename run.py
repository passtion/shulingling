# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tornado.ioloop
import tornado.web
import os
import pyautogui

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render('test.html')
class EnterHandler(tornado.web.RequestHandler):
    def post(self):
        # self.write("Hello, world")
        keyword = self.get_argument('keyword')
        if "+" in keyword:
        	keywordlist = keyword.split("+")
        	if len(keywordlist) == 2:
        		pyautogui.hotkey(keywordlist[0],keywordlist[1])
        		print "keydown {0} {1}".format(keywordlist[0],keywordlist[1])
        else:
            pyautogui.keyDown(keyword)
            # pyautogui.press(keyword)
            print "keydown {0}".format(keyword)
        self.render('test.html')

class XYClickHandler(tornado.web.RequestHandler):
    def post(self):
        # self.write("Hello, world")
        x = self.get_argument('keywordx')
        print x
        y = self.get_argument('keywordy')
        pyautogui.click(int(x), int(y), button='left')
        print "keydown x {0} y {1} left click".format(x,y)
        self.render('test.html')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/enterpress", EnterHandler),
        (r"/xyclick", XYClickHandler),
    ],
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    static_path=os.path.join(os.path.dirname(__file__), 'static'),
    # debug = True,
 #    settings = {
 #    'cookie_secret':'0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
 #    'xsrf_cookies':False,
 #    'login_url':'/login',
 #    'debug':True,
	# }
	)

if __name__ == "__main__":
    app = make_app()
    # app.listen(80)
    app.listen(80,address="0.0.0.0")
    # app.listen(8088,address="192.168.1.104")
    tornado.ioloop.IOLoop.current().start()