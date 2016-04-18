#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Name    : base.py
# @Date    : 2016-04-15 18:06
# @Author  : mengx@shujutiyu.com
# @Link    : http://www.shujutiyu.com
# @Version :

import tornado.web

class RequestHandler(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):
        if status_code == 401:
            self.finish("401 Unauthorized")
        else:
            super(RequestHandler, self).write_error(status_code, **kwargs)