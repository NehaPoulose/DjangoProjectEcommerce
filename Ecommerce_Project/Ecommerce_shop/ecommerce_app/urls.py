from  .import views
from django.urls import path
app_name ='ecommerce_app'

urlpatterns = [
        # path('',views.index,name = "Index"),
        path('',views.allProductCategory,name='allProductCategory'),
        path('<slug:c_slug>/',views.allProductCategory,name = 'Product Collection'),
        path('<slug:c_slug>/<slug:product_slug>/',views.ProductDetail,name = 'Productdetails')
]
