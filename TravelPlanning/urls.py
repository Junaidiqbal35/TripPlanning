from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import SignUpView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('core.urls')),
                  path("accounts/signup/", SignUpView.as_view(), name='signup'),
                  path("accounts/", include("django.contrib.auth.urls")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
