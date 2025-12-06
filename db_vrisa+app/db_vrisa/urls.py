from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Todas las URLs de la app vrisa, con namespace "vrisa"
    path("", include(("vrisa.urls", "vrisa"), namespace="vrisa")),
]
