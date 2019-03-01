from rest_framework.generics import ListAPIView
from apps.content_inspector.models import CrawledContent
from .serializers import CrawlContentSerializer

class CrawledContentAPIView(ListAPIView):
    queryset = CrawledContent.objects.all()
    serializer_class = CrawlContentSerializer
