from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Acheteur(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    type_acheteur = models.CharField(max_length=200, null=True)
    numero_cni = models.CharField(max_length=200, null=True)
    numero_oncc = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=200, null=True)
    filiale = models.CharField(max_length=200, null=True)
    coordonnees_geographiques = models.CharField(max_length=200, null=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'acheteur'
        verbose_name_plural = 'acheteurs'
    def __str__(self):
        return self.nom
    

class Sac(models.Model):
    '''Model definition for Sac.'''
    
    code_qr = models.ImageField(max_length=200, null=True, upload_to='images/')
    quantite = models.FloatField(null=True)
    date_creation = models.DateField(null=True)
    date_modification = models.DateField(null=True)
    acheteur = models.ForeignKey(Acheteur, related_name='acheteur', on_delete=models.CASCADE, null=True)
    
    class Meta:
        '''Meta definition for Sac.'''

        verbose_name = 'Sac'
        verbose_name_plural = 'Sacs'

    def __str__(self):
        return f"Sac {self.quantite}"


class Cooperative(models.Model):
    '''Model definition for Cooperative.'''
    
    nom = models.CharField(max_length=200, null=True)
    image = models.CharField(null=True)
    type_cooperative = models.CharField(max_length=200, null=True)
    siege_social = models.CharField(max_length=200, null=True)
    nom_responssable = models.CharField(max_length=200, null=True)
    contact_responssable = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    departement = models.CharField(max_length=200, null=True)
    arrondissement = models.CharField(max_length=200, null=True)
    village = models.CharField(max_length=200, null=True)
    coordonnees_gps = models.CharField(max_length=200, null=True)
    # identifiant_unique = models.CharField(max_length=500, null=True)
    password = models.CharField(max_length=200, null=True)

    class Meta:
        '''Meta definition for Cooperative.'''

        verbose_name = 'Cooperative'
        verbose_name_plural = 'Cooperatives'

    def __str__(self):
        return self.nom

class Producteur(models.Model):
    '''Model definition for Producteur.'''
    id = models.AutoField(primary_key=True)
    identifiant = models.CharField(max_length=500, null=True)
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    date_naissance = models.CharField(max_length=200, null=True)
    lieu_naissance = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=200, null=True)
    numero_cni = models.CharField(max_length=200, null=True)
    identifiant_fodecc_cicc = models.CharField(max_length=200, null=True)
    numero_telephone = models.CharField(max_length=200, null=True)
    tel_second = models.CharField(max_length=200, null=True)
    an_enreg = models.CharField(max_length=200, null=True)
    nom_cooperative = models.CharField(max_length=200, null=True)
    autre_cooperative = models.CharField(max_length=200, null=True)
    # arrondissement = models.CharField(max_length=200, null=True)
    residence = models.CharField(max_length=200, null=True)
    cooperative = models.ForeignKey(Cooperative, related_name='ProducteurCooperative', on_delete=models.CASCADE, null=True)
    
    

    class Meta:
        '''Meta definition for Producteur.'''

        verbose_name = 'Producteur'
        verbose_name_plural = 'Producteurs'

    def __str__(self):
        return self.nom
    
class Parcelle(models.Model):
    '''Model definition for Parcelle.'''
    numero_titre_foncier = models.CharField(max_length=200, null=True)
    statut = models.CharField(max_length=200, null=True)
    identifiant = models.CharField(max_length=200, null=True)
    superficie = models.FloatField(null=True)
    nombre_arbres = models.IntegerField(null=True)
    age_moyen_arbres = models.FloatField(null=True)
    # producteur_id = models.CharField(max_length=255,null=False)
    geometrie = models.MultiPolygonField(srid=4326, null=True)  # MultiPolygonField pour le type de géométrie
    id_producteur = models.CharField(max_length=200, null=True)
    type_culture = models.CharField(max_length=200, null=True, verbose_name="Type_culture")  # Utilisez des noms de champs en anglais pour éviter des problèmes de casse
    an_creation = models.FloatField(null=True)
    arrondisement = models.CharField(max_length=200, null=True)
    departement = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    longueur = models.FloatField(null=True)
    region = models.CharField(max_length=200,  null=True)
    village = models.CharField(max_length=200,  null=True)
    voie_eau = models.CharField(max_length=200,  null=True)
    url = models.TextField()
    url_carte = models.CharField(max_length=200, null=True)
    producteur = models.ForeignKey(Producteur, related_name='parcelleProducteur', on_delete=models.CASCADE, null=True)
    
    class Meta:
        '''Meta definition for Parcelle.'''

        verbose_name = 'Parcelle'
        verbose_name_plural = 'Parcelles'

    def __str__(self):
        return self.numero_titre_foncier
    
    
    
    
class Lot(models.Model):
    '''Model definition for lot.'''
    
    numero_lot = models.CharField(max_length=200, null=True)
    quantite = models.FloatField()
    type_commercial = models.CharField(max_length=200, null=True)
    urlParcelle = models.CharField(max_length=200, null=True)
    url_carte = models.CharField(max_length=200, null=True)
    taux_humidite = models.FloatField(null=True)
    date_recolt = models.DateField(null=True)
    date_livraison = models.DateField(null=True)
    cooperative = models.ForeignKey(Cooperative, related_name='lotCooperative', on_delete=models.CASCADE, null=True)
    producteur = models.ForeignKey(Producteur, related_name='lotProducteur', on_delete=models.CASCADE, null=True)
    sac = models.ForeignKey(Sac, related_name='lotSac', on_delete=models.CASCADE, null=True)
    parcelle = models.ForeignKey(Parcelle, related_name='lotParcelle', on_delete=models.CASCADE, null=True)
    


    class Meta:
        '''Meta definition for lot.'''

        verbose_name = 'lot'
        verbose_name_plural = 'lots'

    def __str__(self):
        return self.numero_lot

class CooperativeProducteur(models.Model):
    '''Model definition for CooperativeProducteur.'''
    date_arriver_producteur = models.DateField()
    cooperative = models.ForeignKey(Cooperative,related_name='cooperativeProd', on_delete=models.CASCADE, null=True)
    producteur = models.ForeignKey(Producteur, related_name='producteurCoop', on_delete=models.CASCADE, null=True)

    class Meta:
        '''Meta definition for CooperativeProducteur.'''

        verbose_name = 'CooperativeProducteur'
        verbose_name_plural = 'CooperativeProducteurs'



class Utilisateur(models.Model):
    mot_de_passe = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=255, null=True)
    

