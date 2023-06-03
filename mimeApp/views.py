from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
data='''<pre>
<code>
x = 5;
y = 6;
z = x + y;
</code>
</pre>
star
'''

class Htmlview(View):
    def get (self,request):
        return HttpResponse(data,content_type='text/html')

class xmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type='application/xml')


class excelview(View):
    def get(self,request):
        return HttpResponse(data, content_type='application/vnd.ms-excel')





