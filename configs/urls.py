from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('hosts/'),
    path('host/get/<int:ID:>'),
    path('host/add/<int:ID:>'),
    path('host/edit/<int:ID:>'),
    path('host/delete/<int:ID:>'),
]
