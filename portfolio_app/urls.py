from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('contacts',views.contacts,name='contacts'),
    # path('About_Me',views.About_Me,name='About_Me'),
    # path('Education_Details',views.Education_Details,name='Education_Details'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])