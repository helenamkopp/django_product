from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from product.views import home, listProducts, formProducts, listCategories, formCategories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls'))
]