from django.shortcuts import render
from rest_framework import status
from .models import Room ,ROOM_TYPE_CHOICES,STATUS_CHOICES 
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class RoomView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        # Get the 'district' parameter from the query string
        district = request.query_params.get('district', None)

        # Filter rooms based on the district (modify this according to your model structure)
        if district:
            rooms = Room.objects.filter(district=district)
        else:
            rooms = Room.objects.all()
        print(rooms)
        serializer= RoomSerializer(rooms,many=True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)
    
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RoomTypeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,formate=None):
         return Response({'data':[r_type[0] for r_type in ROOM_TYPE_CHOICES]},status=status.HTTP_200_OK)

class RoomStatusView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,formate=None):
         return Response({'data':[s_choice[0] for s_choice in STATUS_CHOICES]},status=status.HTTP_200_OK)


class RoomDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk,format=None):
        try:
         roomlist= Room.objects.get(id=pk)
         serializer= RoomSerializer(roomlist)
         print(roomlist)
         return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Room.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)
    
