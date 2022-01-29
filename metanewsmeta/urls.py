from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from django.urls import re_path

import sentiment_analysis.urls
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home_page'),
    path('admin/', admin.site.urls),
    path('sentiment_analysis/',include(sentiment_analysis.urls)),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


