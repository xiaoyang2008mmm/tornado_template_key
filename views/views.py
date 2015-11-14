#!/usr/bin/python2.6
# -*- coding: utf-8 -*- 
import tornado.web
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db
class Index_Handler(BaseHandler):
    #测试内部apply函数
    def apply_func(self, messages):
	return "<a href>{0}</a>".format(messages)

    #测试用户自定义函数
    def user_func(slef, x ,y):
	   return  str(x) + str(y) 

    def get(self,*args,**kwargs):
	self.ui['test_apply'] = self.apply_func
	print self.__dict__['request'] 
	print self.request.arguments
        self.render('index.html' ,info="</br><h3>测试</h3>", user_func=self.user_func) 

#自定义ui模块函数
class HelloModule(tornado.web.UIModule): 
    def render(self):
        return [ i for i in range(1,10)]



