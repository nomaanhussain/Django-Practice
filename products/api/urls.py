from django.contrib import admin
from django.urls import path
from apps.content_inspector.api.views import CrawledContentAPIView

urlpatterns = [
    path('crawl/', CrawledContentAPIView.as_view(), name='crawl'),
]
