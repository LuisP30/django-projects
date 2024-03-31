from django.contrib import admin
from django.urls import path, include
from index import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),
    path('', views.index, name='inicio')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
