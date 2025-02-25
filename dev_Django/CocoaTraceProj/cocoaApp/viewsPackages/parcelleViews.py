from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Parcelle, Sac, Lot
from cocoaApp.serializer import ParcelleSerializer

class ParcelleCreateView(APIView):
    def post(self, request):
        serializer = ParcelleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ParcelleListView(generics.ListAPIView):
    queryset = Parcelle.objects.all()
    serializer_class = ParcelleSerializer
    
    
class ParcelleByProducteurView(generics.ListAPIView):
    serializer_class = ParcelleSerializer

    def get_queryset(self):
        producteur_id = self.kwargs['producteur_id']
        return Parcelle.objects.filter(producteur_id=producteur_id)
    


class ParcelleUpdateView(generics.UpdateAPIView):
    queryset = Parcelle.objects.all()
    serializer_class = ParcelleSerializer
    lookup_field = 'id'  # Utiliser l'ID du Parcelle pour les opérations

class ParcelleDeleteView(generics.DestroyAPIView):
    queryset = Parcelle.objects.all()
    serializer_class = ParcelleSerializer
    lookup_field = 'id'  # Utiliser l'ID du Parcelle pour les opérations
    
    
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_parcelles_by_cooperative(request, cooperative_id):
    try:
        # Récupérer les IDs des sacs associés à la coopérative
        producteurs = Producteur.objects.filter(cooperative_id=cooperative_id)
        sacs = Sac.objects.filter(id__in=lots.values('sac_id'))
        
        # Récupérer les acheteurs associés aux sacs
        acheteurs = Acheteur.objects.filter(id__in=sacs.values('acheteur_id'))
        
        serializer = AcheteurSerializer(acheteurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class ParcelleByCooperativeAPIView(APIView):
    def get(self, request, cooperative_id):
        # Récupérer les parcelles associées à la coopérative via les lots
        parcelles = Parcelle.objects.filter(lot__cooperative_id=cooperative_id)

        if not parcelles.exists():
            return Response({"message": "Aucune parcelle trouvée pour cette coopérative."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ParcelleSerializer(parcelles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ParcelleByProducteurView(APIView):
    def get(self, request, producteur_id):
        # Récupérer les parcelles associées au producteur
        parcelles = Parcelle.objects.filter(id_producteur=producteur_id)

        if not parcelles.exists():
            return Response({"message": "Aucune parcelle trouvée pour ce producteur."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ParcelleSerializer(parcelles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    

class ParcelleListAPIView(generics.ListAPIView):
    serializer_class = ParcelleSerializer

    def get_queryset(self):
        sac_id = self.kwargs['sac_id']
        try:
            # Récupérer les lots associés au sac
            lots = Lot.objects.filter(sac_id=sac_id)
            # Récupérer les parcelles associées aux lots
            return Parcelle.objects.filter(lotParcelle__in=lots)
        except Sac.DoesNotExist:
            return Parcelle.objects.none()
