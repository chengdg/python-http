#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Name    : server.py
# @Date    : 2016-04-13 11:17
# @Author  : mengx@shujutiyu.com
# @Link    : http://www.shujutiyu.com
# @Version :

import os
import sys
import socket

import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("address", default='0.0.0.0', help="run on the given address", type=str)
define("port", default=8100, help=u"run on the given port")


conf = {
    "debug": True,
}

if __name__ == "__main__":

    sys.path.append(os.path.join(os.path.dirname(__file__), "handlers"))

    from conf import urls

    conf["handlers"] = urls.urls
    conf['cookie_secret'] = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="

    tornado.options.parse_command_line()

    app = tornado.web.Application(**conf)
    server = tornado.httpserver.HTTPServer(app)

    server.listen(options.port, address=options.address)

    print "-" * 20
    print "      tornado run address:%s:%s" % (options.address, options.port)
    print "      wait connect......"
    print "-" * 20

    tornado.ioloop.IOLoop.instance().start()
