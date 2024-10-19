from django.urls import path,include
from .views import ProductApiView,ProductTypeApiView,ProductTypeApiDetailView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'ProductType', ProductApiView)
urlpatterns=router.urls    
urlpatterns = [
    path('product/',ProductApiView.as_view({'get':'list','post':'create'})),
    path('product/<int:pk>/',ProductApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('product-type/',ProductTypeApiView.as_view()),
    path('product-type/<int:pk>/', ProductTypeApiDetailView.as_view())
   
]            
                           
                   
