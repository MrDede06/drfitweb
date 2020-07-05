from django.urls import path
from . import views
from . import spor
from . import diet

app_name = "backend"

urlpatterns = [
    path("", views.yonetim, name="yonetim"),
    path("logout/", views.logout_request, name="logout"),
    path("spor_main/", views.spor_main, name="spor_main"),
    path("diet_main/", views.diet_main, name="diet_main"),
    path("spor_main/spor_kategori/", spor.kategori_ekle, name="spor_kategori_ekle"),
    path("spor_main/spor_altkategori/", spor.altkategori_ekle, name="spor_altkategori_ekle"),
    path("spor_main/spor_programlist/", spor.programlist, name="spor_programlist"),
    path("diet_main/diet_kategori/", diet.kategori_ekle, name="spor_kategori_ekle"),
    path("diet_main/diet_altkategori/", diet.altkategori_ekle, name="spor_altkategori_ekle"),
    path("diet_main/diet_programlist/", diet.programlist, name="spor_programlist"),
    path("spor_main/form_test/", spor.form_test, name="form_test")
]