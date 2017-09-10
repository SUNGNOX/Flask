# -*- coding: utf-8 -*-
def application(environ, start_response):
    start_response('300 0k', [('Content-Type', 'text/html')])#第一个参数为HTTP响应码,不是固定值，第二个参数为HTTP Header
    return ['hello %s!!' % (environ['PATH_INFO'][1:] or 'web')]