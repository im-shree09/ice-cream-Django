from django.contrib import admin
from django.urls import path,include

admin.site.site_header= "Shree ice cream admin"
admin.site.site_header= "Shree ice cream admin portal"
admin.site.index_title= "Welcome to Shree ice creams"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
