from rest_framework import serializers
from .models import Acheteur, Sac, Producteur, Parcelle, Cooperative, Lot, CooperativeProducteur, Utilisateur

        
class AcheteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acheteur
        fields = '__all__'
        
class SacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sac
        fields = '__all__'
        
    #     fields = ['id', 'code_qr', 'quantite', 'date_creation', 'date_modification', 'acheteur']

    # def create(self, validated_data):
    #     # Récupérer les IDs des lots à mettre à jour
    #     lots_ids = validated_data.pop('lots', [])
    #     sac = Sac.objects.create(**validated_data)  # Créer le sac
        
    #     # Mettre à jour les lots pour qu'ils réfèrent au nouveau sac
    #     if lots_ids:
    #         Lot.objects.filter(id__in=lots_ids).update(sac=sac)

        # return sac
    
    
class ProducteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producteur
        fields = '__all__'
class ParcelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcelle
        fields = '__all__'
        
class CooperativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperative
        fields = '__all__'
        
class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__'
        
class CooperativeProducteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = CooperativeProducteur
        fields = '__all__'
        
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'email', 'mot_de_passe']