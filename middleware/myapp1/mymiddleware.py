from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class Test(MiddlewareMixin):
        def process_exception(self, request, exception):
                    print("this is  process_exception")
                    print(exception)
