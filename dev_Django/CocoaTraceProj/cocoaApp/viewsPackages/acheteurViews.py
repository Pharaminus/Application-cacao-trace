from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Acheteur, Sac
from cocoaApp.serializer import AcheteurSerializer
from rest_framework.decorators import api_view

class AcheteurCreateView(APIView):
    def post(self, request):
        serializer = AcheteurSerializer(data=request.data)
        if serializer.is_valid():
            acheteur = serializer.save()
            sacs_ids = request.data.get('sacs', [])
            # Ajouter l'ID de l'acheteur à chaque sac sélectionné
            if sacs_ids:
                sacs = Sac.objects.filter(id__in=sacs_ids)
                # print(f"====( {sacs })=====")
                
                sacs.update(acheteur=acheteur)  # Mettre à jour les sacs pour refléter l'acheteur

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AcheteurListView(generics.ListAPIView):
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerializer
    
    

class AcheteurUpdateView(generics.UpdateAPIView):
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerializer
    lookup_field = 'id'  # Utiliser l'ID du Acheteur pour les opérations

class AcheteurDeleteView(generics.DestroyAPIView):
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerializer
    lookup_field = 'id'  # Utiliser l'ID du Acheteur pour les opérations

    
class AcheteurListView(generics.ListAPIView):
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerializer
    
@api_view(['GET'])
def get_acheteurs_by_cooperative(request, cooperative_id):
    try:
        # Récupérer les IDs des sacs associés à la coopérative
        lots = Lot.objects.filter(cooperative_id=cooperative_id)
        sacs = Sac.objects.filter(id__in=lots.values('sac_id'))
        acheteurs = Acheteur.objects.filter(id__in=sacs.values('acheteur_id'))
        
        serializer = AcheteurSerializer(acheteurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)