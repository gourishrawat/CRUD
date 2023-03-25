from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name=''),
    path('save',views.save),
    path('login',views.login),
    path('log',views.log),
    path('delete/<int:id>/',views.delete,name='delete') ,
    path('logout',views.logout,name='logout') ,
    path('update/<int:id>/',views.update,name='update') ,
    path('uupdate/<int:id>/',views.uupdate,name='uupdate'),
    
    
]
