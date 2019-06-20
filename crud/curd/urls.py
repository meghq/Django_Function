from django.conf.urls import  url

from curd.views import adding,get,onedata,update,delete


urlpatterns =[
    url(r'^adding',adding),
    url(r'^get',get),
    url(r'^one', onedata),
    url(r'^up', update),
    url(r'^del', delete)
]