# readers_haven/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This routes all /api/ traffic to your inventory app
    path('api/', include('inventory.urls')), 
    
]