from django.urls import path
from . import views
from . import spor

app_name = "backend"

urlpatterns = [
    path("", views.yonetim, name="yonetim"),
    path("logout/", views.logout_request, name="logout"),
    path("spor_main/", views.spor_main, name="spor_main"),
    path("spor_main/spor_kategori/", spor.kategori_ekle, name="spor_kategori_ekle"),
    path("spor_main/spor_altkategori/", spor.altkategori_ekle, name="spor_altkategori_ekle"),
    path("spor_main/form_test/", spor.form_test, name="form_test")
]