# views.py

from rest_framework import generics
from rest_framework.response import Response
from cocoaApp.models import Lot, Sac, Producteur, Parcelle, Cooperative, Acheteur
from cocoaApp.serializer import LotSerializer, SacSerializer, ProducteurSerializer, ParcelleSerializer, AcheteurSerializer

class CooperativeDetailView(generics.RetrieveAPIView):
    queryset = Cooperative.objects.all()
    serializer_class = None  # Pas besoin d'un serializer ici

    def get(self, request, *args, **kwargs):
        cooperative_id = kwargs['cooperative_id']
        
        # Récupérer les objets associés
        producteurs = Producteur.objects.filter(cooperative_id=cooperative_id)
        lots = Lot.objects.filter(cooperative_id=cooperative_id)
        # sacs = Sac.objects.filter(acheteur__in=lots.values('id'))
        # if not lots.exists():
            # return Response({'error': 'Aucun lot trouvé avec cet ID.'}, status=status.HTTP_404_NOT_FOUND)
        sacs = Sac.objects.filter(id__in=lots.values('sac_id'))
        parcelles = Parcelle.objects.filter(producteur__in=producteurs.values('id'))
        acheteurs = Acheteur.objects.filter(id__in=sacs.values('acheteur_id'))
        
        # acheteurs = Acheteur.objects.filter(sac__in=sacs.values('id'))

        # Sérialiser les données
        producteurs_data = ProducteurSerializer(producteurs, many=True).data
        lots_data = LotSerializer(lots, many=True).data
        sacs_data = SacSerializer(sacs, many=True).data
        parcelles_data = ParcelleSerializer(parcelles, many=True).data
        acheteurs_data = AcheteurSerializer(acheteurs, many=True).data

        # print(f"=======(sac acheteur : {acheteurs_data}")

        # Retourner la réponse
        return Response({
            'producteur': producteurs_data,
            'sac': sacs_data,
            'lot': lots_data,
            'parcelle': parcelles_data,
            'acheteur': acheteurs_data,
        })