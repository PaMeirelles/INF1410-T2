from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include_docs_urls(title='Documentação da API')),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("api/v1/", include(routers.DefaultRouter().urls)),
    path("openapi/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("schema/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("blog/", include("blog_app.urls")),
    path("api/", include("blog_app.urls")),
    path("auth/", include("authentication.urls")),
]
