from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MobileDeviceSerializer
from .models import MobileDeviceModel


class MobileDeviceView(APIView):


	def post(self, request):
		serializer = MobileDeviceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"status_code": status.HTTP_200_OK, "message":"SUCCESS", "data": serializer.data})
		else:
			return Response({"status_code": status.HTTP_400_BAD_REQUEST,"message": "ERROR", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


	def get(self, request, id=None):

		if id:
			device_details = MobileDeviceModel.objects.get(id=id)
			serializer = MobileDeviceSerializer(device_details)
			return Response({"status_code": status.HTTP_200_OK, "message": "SUCCESS", "data": serializer.data})


		device_details = MobileDeviceModel.objects.all()
		serializer = MobileDeviceSerializer(device_details, many=True)
		return Response({"status_code": status.HTTP_200_OK, "message": "SUCCESS", "data": serializer.data})

	def patch(self, request, id=None):
		device_details = MobileDeviceModel.objects.get(id=id)
		serializer = MobileDeviceSerializer(device_details, request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({"status_code": status.HTTP_200_OK, "message":"SUCCESS", "data":serializer.data})
		else:
			return Response({"status_code": status.HTTP_400_BAD_REQUEST, "message":"ERROR", "data":serializer.errors})
	
	def delete(self, request, id=None):
		from django.shortcuts import get_object_or_404
		item = get_object_or_404(MobileDeviceModel, id=id)
		item.delete()
		return Response({"status": "success", "data": "Item Deleted"})
