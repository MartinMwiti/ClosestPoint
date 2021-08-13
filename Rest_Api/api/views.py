from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Points
from . serializers import PointsSerializer
from . closestDistance import getClosestDistance


class closestDistanceValue(APIView):

    def get(self, request):
        points = Points.objects.all()
        # serializer is used to take all the objects & convert to JSON. 'many=True' returns more than one JSON object. e.g. [{}, {}]
        serializer = PointsSerializer(points, many=True)

        # returns/render into JSON type instead of http response
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            points = request.data  # user input
            # convert input into a string. Datatype for point in the model is of Charfield
            s = str(points['string_points'])
            # print('The value of s is:', s)
            closestPoint = getClosestDistance(s) # calculate closest distance
            # print("closestPoint value is:", closestPoint)
            data = {
                'point': s,
                'closestPoint': closestPoint
            }  # create a Python dictionary

            # save to db
            # convert the Python dictionary to model instance
            serializer = PointsSerializer(data=data)
            if serializer.is_valid():  # check for validity based on model instance datatypes
                serializer.save()  # save to db
                # Return closest distance value in a JSON format and status 200
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                    return "Problem with your values"
        except  BaseException(e):
            # Return status 400 if the input is not a valid entry
            return Response(status=status.HTTP_400_BAD_REQUEST)
