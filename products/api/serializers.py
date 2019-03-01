from rest_framework import serializers
from apps.content_inspector.models import CrawledContent


class CrawlContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawledContent
        fields = [
            '_id',
            'title',
            'siteName',    
            'origin',
            'link',
        ]