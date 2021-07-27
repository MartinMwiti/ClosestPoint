from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Points
from . serializers import PointsSerializer
from . closestDistance import getClosestDistance


class employeeList(APIView):

    def get(self, request): 
        points = Points.objects.all()
        serializer = PointsSerializer(points, many=True)  # serializer is used to take all the objects & convert to JSON. 'many=True' returns more than one JSON object.

        return Response(serializer.data) # returns JSON instead of http response

    def post(self, request, format=None):
        string_points=request.data
        s = str(string_points['string_points'])
        print('The value of s is:', s)
        closestPoint = getClosestDistance(s)
        print("closestPoint value is:", closestPoint)
        data = {
            'point': s,
            'closestPoint': closestPoint
        }
        
        # save to db
        serializer = PointsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
        
