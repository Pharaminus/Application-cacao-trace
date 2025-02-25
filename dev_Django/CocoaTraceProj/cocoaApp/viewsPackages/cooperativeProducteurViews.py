from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import CooperativeProducteur
from cocoaApp.serializer import CooperativeProducteurSerializer

class CooperativeProducteurCreateView(APIView):
    def post(self, request):
        serializer = CooperativeProducteurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CooperativeProducteurListView(generics.ListAPIView):
    queryset = CooperativeProducteur.objects.all()
    serializer_class = CooperativeProducteurSerializer
    
    
class CooperativeProducteurByProducteurView(generics.ListAPIView):
    serializer_class = CooperativeProducteurSerializer

    def get_queryset(self):
        producteur_id = self.kwargs['producteur_id']
        return CooperativeProducteur.objects.filter(producteur_id=producteur_id)

class CooperativeProducteurByCooperativeView(generics.ListAPIView):
    serializer_class = CooperativeProducteurSerializer

    def get_queryset(self):
        cooperative_id = self.kwargs['cooperative_id']
        return CooperativeProducteur.objects.filter(cooperative_id=cooperative_id)


class CooperativeProducteurUpdateView(generics.UpdateAPIView):
    queryset = CooperativeProducteur.objects.all()
    serializer_class = CooperativeProducteurSerializer
    lookup_field = 'id'  # Utiliser l'ID du CooperativeProducteur pour les opérations

class CooperativeProducteurDeleteView(generics.DestroyAPIView):
    queryset = CooperativeProducteur.objects.all()
    serializer_class = CooperativeProducteurSerializer
    lookup_field = 'id'  # Utiliser l'ID du CooperativeProducteur pour les opérations