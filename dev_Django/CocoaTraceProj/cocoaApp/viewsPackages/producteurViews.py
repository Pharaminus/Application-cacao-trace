from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Producteur
from cocoaApp.serializer import ProducteurSerializer

class ProducteurCreateView(APIView):
    def post(self, request):
        print(f"=========| {request.data}")
        serializer = ProducteurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
class ProducteurListView(generics.ListAPIView):
    queryset = Producteur.objects.all()
    serializer_class = ProducteurSerializer
    
    
class ProducteurByCooperativeView(generics.ListAPIView):
    serializer_class = ProducteurSerializer

    def get_queryset(self):
        cooperative_id = self.kwargs['cooperative_id']
        return Producteur.objects.filter(producteurCoop__cooperative_id=cooperative_id)
    


class ProducteurUpdateView(generics.UpdateAPIView):
    queryset = Producteur.objects.all()
    serializer_class = ProducteurSerializer
    lookup_field = 'id'  # Utiliser l'ID du producteur pour les opérations

class ProducteurDeleteView(generics.DestroyAPIView):
    queryset = Producteur.objects.all()
    serializer_class = ProducteurSerializer
    lookup_field = 'id'  # Utiliser l'ID du producteur pour les opérations
    
    
class ProducteurByCooperativeAPIView(APIView):
    def get(self, request, cooperative_name):
        producteurs = Producteur.objects.filter(cooperative=cooperative_name)

        if not producteurs.exists():
            return Response({"message": "Aucun producteur trouvé pour cette coopérative."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProducteurSerializer(producteurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)