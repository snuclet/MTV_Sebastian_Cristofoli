from django.http import HttpResponse
from django.template import Template, Context

def familia(request):
    return HttpResponse

def my_template(request):
   
    my_html = open("C:/Users/Sebastián/Desktop/Seba/MTV_Sebastian_Cristofoli/Template/template.html")

    template = Template(my_html.read().encode("latin-1").decode("utf-8")) 
    context = Context()
    render = template.render(context) 

    my_html.close() 
    return HttpResponse(render)