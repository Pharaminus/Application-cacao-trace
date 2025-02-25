from django.urls import  path, include
from cocoaApp.viewsPackages.sacViews import * 
from cocoaApp.viewsPackages.parcelleViews import ParcelleCreateView, ParcelleListView,ParcelleByProducteurView, ParcelleUpdateView, ParcelleDeleteView, ParcelleByCooperativeAPIView, ParcelleByProducteurView, ParcelleListAPIView
from cocoaApp.viewsPackages.producteurViews import ProducteurCreateView, ProducteurListView, ProducteurByCooperativeView, ProducteurUpdateView, ProducteurDeleteView
from cocoaApp.viewsPackages.acheteurViews import AcheteurCreateView, AcheteurListView, AcheteurUpdateView, AcheteurDeleteView, get_acheteurs_by_cooperative
from cocoaApp.viewsPackages.cooperativeViews import CooperativeCreateView, CooperativeListView, CooperativeUpdateView, CooperativeDeleteView
from cocoaApp.viewsPackages.lotViews import *
from cocoaApp.viewsPackages.cooperativeProducteurViews import CooperativeProducteurCreateView, CooperativeProducteurListView, CooperativeProducteurUpdateView, CooperativeProducteurDeleteView, CooperativeProducteurByCooperativeView, CooperativeProducteurByProducteurView
from rest_framework.routers import DefaultRouter
from .views import *
from cocoaApp.viewsPackages.cooperativeApiView import CooperativeDetailView



router = DefaultRouter()
router.register(r'sacs', SacViewSet)
router.register(r'lots', LotViewSet)



# ===========| acheteur urls |========================
AcheteurRouteur = DefaultRouter()


# AcheteurRouteur.register('acheteur_rest', AcheteurViewset, basename='acheteur_viewset' )
urlpatterns = [
    path('cocoa/login/', LoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
    # path('cocoa/cooperative/<int:cooperative_id>/data/', get_all_data_by_cooperative, name='get_all_data_by_cooperative'),
    path('cocoa/cooperatives/<int:cooperative_id>/', CooperativeDetailView.as_view(), name='cooperative-detail'),

    path('cocoa/acheteur/new/', AcheteurCreateView.as_view(), name='acheteur-create'),
    path('cocoa/acheteur/list/', AcheteurListView.as_view(), name='acheteur-list'),
    # path('cocoa/cooperatives/<int:cooperative_id>/acheteur/', AcheteurByCooperativeView.as_view(), name='producers-by-cooperative'),
    path('cocoa/acheteur/<int:id>/', AcheteurUpdateView.as_view(), name='acheteur-update'),
    path('cocoa/acheteur/<int:id>/delete/', AcheteurDeleteView.as_view(), name='acheteur-delete'),
    path('cocoa/acheteur/cooperative/<int:cooperative_id>/', get_acheteurs_by_cooperative, name='get_acheteurs_by_cooperative'),
]
urlpatterns += AcheteurRouteur.urls + router.urls

# ===========| login-logout urls |========================
loginRouteur = DefaultRouter()
from .views import login_view, logout_view, check_authentication, get_csrf_token

login_urls = [
    path("api/csrf/", get_csrf_token, name="csrf"),
    path("api/login/", login_view, name="login"),
    path("api/logout/", logout_view, name="logout"),
    path("api/check-auth/", check_authentication, name="check-auth"),
]
urlpatterns += login_urls + loginRouteur.urls


# ===========| sac urls |========================
sacRouteur = DefaultRouter()
# sacRouteur.register('sac_rest', SacViewset, basename='sac_viewset' )
sac_urls = [
    path('cocoa/sac/new/', SacCreateView.as_view(), name='sac-create'),
    path('cocoa/sac/creat/', SacCreateView.as_view(), name='sac-create'),
    path('cocoa/sac/list/', SacListView.as_view(), name='sac-list'),
    path('cocoa/cooperatives/<int:cooperative_id>/sac/', SacByAcheteurView.as_view(), name='producers-by-cooperative'),
    path('cocoa/sac/<int:id>/', SacUpdateView.as_view(), name='sac-update'),
    path('cocoa/sac/<int:id>/delete/', SacDeleteView.as_view(), name='sac-delete'),
    path('cocoa/sacs/acheteur/<int:acheteur_id>/', get_sacs_by_acheteur, name='get_sacs_by_acheteur'),
    path('cocoa/sac/cooperative/<int:cooperative_id>/', SacByCooperativeView.as_view(), name='sacs_by_cooperative'),
    path('cocoa/sac/<int:sac_id>/lot/', LotListAPIView.as_view(), name='lot-list'),
    path('cocoa/sac-free/list/<int:cooperative_id>/', SacByCooperativeView.as_view(), name='lot-list'),
    # path('cocoa/sac-free/list/', SacNonAchete.as_view(), name='lot-list'),
]   
urlpatterns += sac_urls + sacRouteur.urls


# ===========| producteur urls |========================
producteurRouteur = DefaultRouter()
# producteurRouteur.register('producteur_rest', ProducteurViewset, basename='producteur_viewset' )
producteur_urls = [
    path('cocoa/producteur/new/', ProducteurCreateView.as_view(), name='producteur-create'),
    path('cocoa/producteur/list/', ProducteurListView.as_view(), name='producteur-list'),
    path('cocoa/producteur/cooperative/<int:cooperative_id>/', ProducteurByCooperativeView.as_view(), name='producers-by-cooperative'),
    path('cocoa/producteur/<int:id>/', ProducteurUpdateView.as_view(), name='producteur-update'),
    path('cocoa/producteur/<int:id>/delete/', ProducteurDeleteView.as_view(), name='producteur-delete'),
]
urlpatterns += producteur_urls + producteurRouteur.urls



# ===========| parcelle urls |========================
parcelleRouteur = DefaultRouter()
# parcelleRouteur.register('parcelle_rest', ParcelleViewset, basename='parcelle_viewset' )
parcelle_urls = [
    path('sac/<int:sac_id>/parcelles/', ParcelleListAPIView.as_view(), name='parcelle-list'),
    path('cocoa/parcelles/producteur/<str:producteur_id>/', ParcelleByProducteurView.as_view(), name='parcelles_by_producteur'),
    path('cocoa/parcelle/cooperative/<int:cooperative_id>/', ParcelleByCooperativeAPIView.as_view(), name='parcelles_by_cooperative'),
    path('cocoa/parcelle/new/', ParcelleCreateView.as_view(), name='parcelle-create'),
    path('cocoa/parcelle/list/', ParcelleListView.as_view(), name='parcelle-list'),
    path('cocoa/parcelle/cooperative/<int:cooperative_id>/', ParcelleByProducteurView.as_view(), name='producers-by-cooperative'),
    path('cocoa/parcelle/<int:id>/', ParcelleUpdateView.as_view(), name='parcelle-update'),
    path('cocoa/parcelle/<int:id>/delete/', ParcelleDeleteView.as_view(), name='parcelle-delete'),
]
urlpatterns += parcelle_urls + parcelleRouteur.urls



# ===========| cooperative urls |========================
cooperativeRouteur = DefaultRouter()
# cooperativeRouteur.register('cooperative_rest', CooperativeViewset, basename='cooperative_viewset' )
cooperative_urls = [
    path('cocoa/cooperative/new/', CooperativeCreateView.as_view(), name='cooperative-create'),
    path('cocoa/cooperative/list/', CooperativeListView.as_view(), name='cooperative-list'),
    # path('cocoa/cooperatives/<int:cooperative_id>/cooperative/', CooperartiveByCooperativeView.as_view(), name='producers-by-cooperative'),
    path('cocoa/cooperative/<int:id>/', CooperativeUpdateView.as_view(), name='cooperative-update'),
    path('cocoa/cooperative/<int:id>/delete/', CooperativeDeleteView.as_view(), name='cooperative-delete'),
]
urlpatterns += cooperative_urls + cooperativeRouteur.urls

# ===========| lot urls |========================
lotRouteur = DefaultRouter()
# lotRouteur.register('lot_rest', lotViewset, basename='lot_viewset' )
lot_urls = [
    path('cocoa/lot/new/', LotCreateView.as_view(), name='lot-create'),
    path('cocoa/lot/list/', LotListView.as_view(), name='lot-list'),
    path('cocoa/lot/cooperative/<int:cooperative_id>/', LotByCooperativeAPIView.as_view(), name='lots_by_cooperative'),    path('cocoa/cooperatives/<int:cooperative_id>/lot/', LotByCooperativeView.as_view(), name='producers-by-cooperative'),
    path('cocoa/cooperatives/<int:cooperative_id>/lot/', LotByParcelleView.as_view(), name='producers-by-cooperative'),
    path('cocoa/lot/<int:id>/', LotUpdateView.as_view(), name='lot-update'),
    path('cocoa/lot/<int:id>/delete/', LotDeleteView.as_view(), name='lot-delete'),
    path('cocoa/lot-free/list/', LotNonAchete.as_view(), name='sac-list'),
    
]
urlpatterns += lot_urls + lotRouteur.urls

# ===========| cooperativeProducteur urls |========================
cooperativeProducteurRouteur = DefaultRouter()
# cooperativeProducteurRouteur.register('cooperativeProducteur_rest', cooperativeProducteurViewset, basename='cooperativeProducteur_viewset' )
cooperativeProducteur_urls = [
    path('cocoa/cooperativeProducteur/new/', CooperativeProducteurCreateView.as_view(), name='cooperativeProducteur-create'),
    path('cocoa/cooperativeProducteur/list/', CooperativeProducteurListView.as_view(), name='cooperativeProducteur-list'),
    path('cocoa/cooperatives/<int:cooperative_id>/cooperativeProducteur/', CooperativeProducteurByProducteurView.as_view(), name='producers-by-cooperative'),
    path('cocoa/cooperatives/<int:cooperative_id>/cooperativeProducteur/', CooperativeProducteurByCooperativeView.as_view(), name='producers-by-cooperative'),
    path('cocoa/cooperativeProducteur/<int:id>/', CooperativeProducteurUpdateView.as_view(), name='cooperativeProducteur-update'),
    path('cocoa/cooperativeProducteur/<int:id>/delete/', CooperativeProducteurDeleteView.as_view(), name='cooperativeProducteur-delete'),
]
urlpatterns += cooperativeProducteur_urls + cooperativeProducteurRouteur.urls

from django.views.generic import TemplateView

urlpatterns2 = [
    path('', TemplateView.as_view(template_name='index.html')),  # Sert React
]

urlpatterns += urlpatterns2



