from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BogieChecksheet, WheelSpecification
from .serializers import BogieChecksheetSerializer, WheelSpecificationSerializer



from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class BogieChecksheetCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BogieChecksheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WheelSpecificationListView(generics.ListAPIView):
    queryset = WheelSpecification.objects.all()
    serializer_class = WheelSpecificationSerializer
