from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mainApp.views import *
from userApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('mainApp.urls')),
    path('user/', include('userApp.urls')),
    path('order/', include('orderApp.urls')),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('', RegisterView.as_view(), name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
