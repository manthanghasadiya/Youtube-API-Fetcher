from django.db import models

class Videos(models.Model):
    video_id = models.CharField(
        null=False,
        blank=False,
        max_length=200
    )

    title = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )

    description = models.CharField(
        null=True,
        blank=True,
        max_length=5000
    )

    publishedDateTime = models.DateTimeField()

    channel_title = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )
    
    thumbnail = models.URLField(max_length=200)