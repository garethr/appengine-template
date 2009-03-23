#!/usr/bin/env python

import os
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from lib import BaseRequest
import settings

webapp.template.register_template_library('filters')

class Index(BaseRequest):
    def get(self):        
        context = {}
        # calculate the template path
        output = self.render("index.html", context)
        self.response.out.write(output)

class NotFoundPageHandler(BaseRequest):
    def get(self):
        self.error(404)
        output = self.render("404.html")
        self.response.out.write(output)

# Log a message each time this module get loaded.
logging.info('Loading %s, app version = %s',
    __name__, os.getenv('CURRENT_VERSION_ID'))
                        
def main():
    "Run the application"
    # wire up the views
    ROUTES = [
        ('/', Index),
        ('/.*', NotFoundPageHandler),
    ]
    application = webapp.WSGIApplication(ROUTES, debug=settings.DEBUG)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()