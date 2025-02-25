from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from cocoaApp.models import Sac, Cooperative
from cocoaApp.serializer import SacSerializer, LotSerializer, Lot

from rest_framework.decorators import api_view
from rest_framework import status

import qrcode

import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from io import BytesIO


class SacCreateView(APIView):
    
    def post(self, request):
        serializer = SacSerializer(data=request.data)  # Utilisez le sérialiseur pour Sac
        
        if serializer.is_valid():
            sac = serializer.save()  # Sauvegarde du sac
            
            lots_ids = request.data.get('lots', [])  # Obtenir les IDs des lots
            # Si des lots sont fournis, mettre à jour leur champ 'sac'
            print(f"====|{lots_ids } |===")
            if lots_ids:
                lots = Lot.objects.filter(id__in=lots_ids)
                lots.update(sac=sac)  # Mettre à jour le champ 'sac' dans Lot

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def post(self, request):
    #     serializer = SacSerializer(data=request.data)
    #     if serializer.is_valid():
    #         sac = serializer.save()  # Sauvegarder le sac
            
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SacListView(generics.ListAPIView):
    queryset = Sac.objects.all()
    serializer_class = SacSerializer
    
    
class SacByAcheteurView(generics.ListAPIView):
    serializer_class = SacSerializer

    def get_queryset(self):
        acheteur_id = self.kwargs['acheteur_id']
        return Sac.objects.filter(acheteur_id=acheteur_id)
    


class SacUpdateView(generics.UpdateAPIView):
    queryset = Sac.objects.all()
    serializer_class = SacSerializer
    lookup_field = 'id'  # Utiliser l'ID du Sac pour les opérations

class SacDeleteView(generics.DestroyAPIView):
    queryset = Sac.objects.all()
    serializer_class = SacSerializer
    lookup_field = 'id'  # Utiliser l'ID du Sac pour les opérations
    




@csrf_exempt
@api_view(['POST'])
def create_sac(request):
    if request.method == 'POST':
        quantite = request.data.get('quantite')
        acheteur_id = request.data.get('acheteur')
        date_creation = request.data.get('date_creation')
        date_modification = request.data.get('date_modification')

        # Générer le code QR
        qr_content = f"Quantité: {quantite}, \nAcheteur ID: {acheteur_id} \ndate_creation {date_creation}, \ndate_modification {date_modification}",
    # Générer le QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_content)
        qr.make(fit=True)

        # Créer une image du QR code
        img = qr.make_image(fill='black', back_color='white')

        # Utiliser BytesIO pour sauvegarder l'image en mémoire
        buffer = BytesIO()
        img.save(buffer, format='PNG')  # Sauvegarder au format PNG
        buffer.seek(0)  # Revenir au début du buffer

        # Créer un fichier content avec le buffer
        image_file = ContentFile(buffer.getvalue(), name=f'sac_{timezone.now().timestamp()}.png')

   

        # Enregistrer le sac dans la base de données
        sac = Sac.objects.create(
            code_qr=image_file,
            quantite=quantite,
            date_creation=timezone.now(),
            date_modification=timezone.now(),
            acheteur_id=acheteur_id
        )

        return JsonResponse({'id': sac.id, 'message': 'Sac créé avec succès!'})
    
    
    
def make_qr_code(self):

        # Générer le QR code
        qr = qrcode.QRCode(
            version=1,  # version=1 signifie la plus petite taille de QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur (L : faible)
            box_size=10,  # Taille de chaque "boîte" du QR code
            border=4,  # Largeur de la bordure
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Créer une image du QR code
        img = qr.make_image(fill='black', back_color='white')
        return img
        img.save("qrcode_site_web.png")
        
        



@api_view(['GET'])
def get_sacs_by_acheteur(request, acheteur_id):
    try:
        sacs = Sac.objects.filter(acheteur_id=acheteur_id)
        serializer = SacSerializer(sacs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def get_acheteurs_by_cooperative(request, cooperative_id):
    try:
        # Récupérer les IDs des sacs associés à la coopérative
        lots = Lot.objects.filter(cooperative_id=cooperative_id)
        sacs = Sac.objects.filter(id__in=lots.values('sac_id'))
        
        # Récupérer les acheteurs associés aux sacs
        acheteurs = Acheteur.objects.filter(id__in=sacs.values('acheteur_id'))
        
        serializer = AcheteurSerializer(acheteurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
# class SacByCooperativeView(APIView):
#     def get(self, request, cooperative_id):
#         # Récupérer les sacs associés à la coopérative
#         sacs = Sac.objects.filter(acheteur__lot__cooperative_id=cooperative_id, acheteur_id__isnull=True)

#         if not sacs.exists():
#             return Response({"message": "Aucun sac trouvé pour cette coopérative."}, status=status.HTTP_404_NOT_FOUND)

#         serializer = SacSerializer(sacs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class SacByCooperativeView(APIView):
    def get(self, request, cooperative_id):
        try:
            # Vérifier si la coopérative existe
            cooperative = Cooperative.objects.filter(id=cooperative_id).first()
            
            if not cooperative:
                return Response({"message": "Coopérative non trouvée."}, status=status.HTTP_404_NOT_FOUND)

            # Filtrer les sacs associés à la coopérative et sans acheteur
            # sacs = Sac.objects.filter(lot__cooperative_id=cooperative_id, acheteur__isnull=True)
            
            # Filtrer les lots associés à la coopérative avec id=4
            lots = Lot.objects.filter(cooperative_id=cooperative_id)

            # Récupérer les sacs associés à ces lots et sans acheteur
            sacs = Sac.objects.filter(lotSac__in=lots, acheteur__isnull=True)
            # sacs = Sac.objects.filter(lotsac__cooperative_id=4, acheteur__isnull=True)
            

            print(f"==(1) { sacs}")

            if not sacs.exists():
                return Response({"message": "Aucun sac trouvé pour cette coopérative sans acheteur."}, status=status.HTTP_404_NOT_FOUND)

            serializer = SacSerializer(sacs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class LotListAPIView(generics.ListAPIView):
    serializer_class = LotSerializer

    def get(self, request, *args, **kwargs):
        sac_id = kwargs['sac_id']
        lots = Lot.objects.filter(sac_id=sac_id)

        lots_data = LotSerializer(lots, many=True).data
        return Response({
            'lot': lots_data,
        })
    

class SacNonAchete(generics.ListAPIView):
    queryset = Sac.objects.filter(acheteur_id__isnull=True)
    serializer_class = SacSerializer
    
from rest_framework import viewsets

    
class SacViewSet(viewsets.ModelViewSet):
    queryset = Sac.objects.all()
    serializer_class = SacSerializer

    def perform_create(self, serializer):
        serializer.save()
