#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Name    : urls.py
# @Date    : 2016-04-14 10:48
# @Author  : mengx@shujutiyu.com
# @Link    : http://www.shujutiyu.com
# @Version :


from tornado.web import url
from handlers.versions.api import VersionHandler, Version1Handler, VersionDocsHandler

urls = [
    url(r'/$', VersionHandler),
    url(r'/v1.0/?$', Version1Handler ),
    url(r'/v1.0/docs/?$', VersionDocsHandler )
]