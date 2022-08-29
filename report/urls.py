from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('excel/',views.generatereport,name="generatereport"),
    path('', views.UploadView.as_view(), name='fileupload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
