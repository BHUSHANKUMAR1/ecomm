from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, serializers, viewsets
from .views import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('signup', views.user_registration, name='signup'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('cart', views.Cart, name='cart'),
    path('price', views.price, name='priceee'),
    path('checkout', views.Checkout, name='checkout'),
    path('Order_dtls', views.Order_dtls, name='Order_dtls'),
    # path('myorder', views.myorder, name='myorder'),
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('table', views.table, name='table'),
    path('tt', views.tt, name='tt'),
    path('find', views.find, name='find'),
    # path('buynow', views.buynow, name='buynow'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
