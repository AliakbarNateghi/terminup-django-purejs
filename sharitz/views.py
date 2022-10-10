from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import courseSerializer, collegeSerializer, wsSerializer
from .models import course, College, ws


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/course-list',
        'college': '/college-list',
        'ws': '/ws-list',
        'Detail View': '/course-detail/<str:pk>/',
        'Create': '/course-create/',
        'Update': '/course-update/<str:pk>/',
        'Delete': '/course-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def courseList(request):
    courses = course.objects.all().order_by('-id')
    serializer = courseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def collegeList(request):
    colleges = College.objects.all().order_by('-id')
    serializer = collegeSerializer(colleges, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def wsList(request):
    wss = ws.objects.all().order_by('-id')
    serializer = wsSerializer(wss, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def courseDetail(request, pk):
    courses = course.objects.get(id=pk)
    serializer = courseSerializer(courses, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def courseCreate(request):
    serializer = courseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def courseUpdate(request, pk):
    courses = course.objects.get(id=pk)
    serializer = courseSerializer(instance=courses, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def courseDelete(request, pk):
    courses = course.objects.get(id=pk)
    courses.delete()

    return Response('Deleted')


