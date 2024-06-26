from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple view for the root URL
def home_view(request):
    return HttpResponse("Welcome to TeamCollab API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('', home_view),  # Add this line to handle the root path
]
