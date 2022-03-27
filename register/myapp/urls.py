from django.urls import path
from django.contrib import admin


from myapp import views

app_name='myapp'
urlpatterns = [
    path('register/',views.register,name='register'),


    path('admin/', admin.site.urls),

]
