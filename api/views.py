from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BogieChecksheet, WheelSpecification
from .serializers import BogieChecksheetSerializer, WheelSpecificationSerializer



from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# ✅ CSRF-exempt dummy POST API
@method_decorator(csrf_exempt, name='dispatch')
class BogieChecksheetCreateView(APIView):
    def post(self, request, *args, **kwargs):
       
     return Response({"message": "Bogie checksheet data received successfully."}, status=status.HTTP_201_CREATED)
# ✅ GET API to list all WheelSpecification objects
class WheelSpecificationListView(generics.ListAPIView):
    queryset = WheelSpecification.objects.all()
    serializer_class = WheelSpecificationSerializer
