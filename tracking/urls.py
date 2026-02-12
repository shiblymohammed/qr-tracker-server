from django.urls import path
from .views import track_scan, scan_stats, locations

urlpatterns = [
    path('q/<slug:code>/', track_scan),
    path('api/stats/', scan_stats),
    path('api/locations/', locations),
]
