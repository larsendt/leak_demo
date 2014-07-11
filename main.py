#!/usr/bin/env python

import web

urls = (
        ".*", "index",
)
app = web.application(urls, globals())

class index:
    def GET(self):
        return "index"

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
