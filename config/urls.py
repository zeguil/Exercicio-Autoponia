#django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#DRF
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

#yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# viewSets
from regadores.api.viewsets import RegadorViewSet
from plantas.api.viewsets import PlantaViewSet
from usuarios.api.viewsets import UsuarioViewSet
router = DefaultRouter()

# rotas de viewsets
router.register('plantas', PlantaViewSet)
router.register('regadores', RegadorViewSet)
router.register('usuarios', UsuarioViewSet)

# configurção do swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API Autoponia",
      default_version='v1',
      description="Exercício Autoponia",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@autoponia.com.br"),
      license=openapi.License(name="All rights reserved"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/token', TokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # faz com que o django abra imagens no navegador