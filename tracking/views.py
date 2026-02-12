from django.shortcuts import redirect, get_object_or_404
from .models import Location, Scan
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count
from .serializers import LocationSerializer


def track_scan(request, code):
    location = get_object_or_404(Location, code=code)

    Scan.objects.create(
        location=location,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT')
    )

    return redirect("http://localhost:5173")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def scan_stats(request):
    data = (
        Scan.objects
        .values('location__name')
        .annotate(total=Count('id'))
        .order_by('-total')
    )
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def locations(request):
    if request.method == 'GET':
        qs = Location.objects.all()
        serializer = LocationSerializer(qs, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
