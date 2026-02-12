from django.urls import path
from .views import track_scan, scan_stats, locations, health_check

urlpatterns = [
    path('q/<slug:code>/', track_scan),
    path('api/stats/', scan_stats),
    path('api/locations/', locations),
    path('api/health/', health_check),
]
