from django.urls import path,include
from rest_framework import routers
from .views import (
    CategoryViewListCreate,
    BrandViewSet,
    CategoryURD,
)

router = routers.DefaultRouter()
router.register("brand",BrandViewSet)


urlpatterns =[
    path("category/",CategoryViewListCreate.as_view()),
    path("category/<int:pk>",CategoryURD.as_view()),
    path("",include(router.urls))
     
]