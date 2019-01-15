#coding=utf-8
from django.utils.deprecation import MiddlewareMixin


class Row1(MiddlewareMixin):
    def process_request(self,request):
        print "process request1"

    def process_response(self,request,response):
        print 'process response1'
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print "process request2"

    def process_response(self,request,response):
        print 'process response2'
        return response

class Row3(MiddlewareMixin):
    def process_request(self,request):
        print "process request3"

    def process_response(self,request,response):
        print 'process response3'
        return response