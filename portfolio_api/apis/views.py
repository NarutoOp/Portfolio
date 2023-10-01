# import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# import local data
from .serializers import GeeksSerializer
from .models import GeeksModel
 
# create a viewset
class GeeksView(APIView):
    # define queryset

    def get(self, request, *args, **kwargs):  
        result = GeeksModel.objects.all() 
        serializers = GeeksSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = GeeksSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):  
        # result = get_object_or_404(GeeksModel, id=id) 
        result = GeeksModel.objects.all() 
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})   