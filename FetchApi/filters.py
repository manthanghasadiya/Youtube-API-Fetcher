import django_filters
from .models import Videos

class video_filter(django_filters.FilterSet):
    class Meta():
        model = Videos
        fields = ['title', 'description', 'channel_title']