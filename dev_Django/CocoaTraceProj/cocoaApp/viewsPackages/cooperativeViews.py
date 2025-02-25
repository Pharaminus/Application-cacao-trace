from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Cooperative
from cocoaApp.serializer import CooperativeSerializer

class CooperativeCreateView(APIView):
    def post(self, request):
        serializer = CooperativeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CooperativeListView(generics.ListAPIView):
    queryset = Cooperative.objects.all()
    serializer_class = CooperativeSerializer
    
    
# class CooperativeByCooperativeView(generics.ListAPIView):
#     serializer_class = CooperativeSerializer

#     def get_queryset(self):
#         cooperative_id = self.kwargs['cooperative_id']
#         return Cooperative.objects.filter(CooperativeCoop__cooperative_id=cooperative_id)
    


class CooperativeUpdateView(generics.UpdateAPIView):
    queryset = Cooperative.objects.all()
    serializer_class = CooperativeSerializer
    lookup_field = 'id'  # Utiliser l'ID du Cooperative pour les opérations

class CooperativeDeleteView(generics.DestroyAPIView):
    queryset = Cooperative.objects.all()
    serializer_class = CooperativeSerializer
    lookup_field = 'id'  # Utiliser l'ID du Cooperative pour les opérations