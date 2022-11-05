from crud import serialize
from .models import DetailsModel
from .serialize import DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class DetailsTable(APIView):
    def get(self,request):
        detailsObj=DetailsModel.objects.all()
        dlSerializeObj=DetailsSerializer(detailsObj,many=True)
        return Response(dlSerializeObj.data)

    def post(self,request):
        serializeObj=DetailsSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors) 

class DetailsUpdate(APIView):
      def post(self,request,pk):
        try:
            detailObj=DetailsModel.objects.get(id=pk)
        except:
            return Response("Not Found")
        serializeObj=DetailsSerializer(detailObj,data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors) 
class DetailsDelete(APIView):
      def post(self,request,pk):
        try:
            detailObj=DetailsModel.objects.get(id=pk)
        except:
            return Response("Not Found")
        detailObj.delete()
        return Response(200) 
