from django.db import models
from django.utils import timezone


# Create your models here.
class BasePublishModel(models.Model):
    class PublishStateOptions(models.TextChoices):
        PUBLISHED = "PU", "PUBLICADO"
        DRAFT = "BR", "BORRADOR"
        PRIVATE = "PR", "PRIVADO"
        
    state = models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False,null=True)
    
    class Meta:
        abstract = True
        ordering = ["-updated", "-timestamp"] 

    def save(self, *args, **kwargs):
        if self.state_is_published and self.publish_timestamp is None:
            self.publish_timestamp = timezone.now()
        else:
            self.publish_timestamp = None
        super().save(*args, **kwargs)

    @property
    def state_is_published(self):
        return self.state == self.PublishStateOptions.PUBLISHED

    def is_published(self):
        publish_timestamp = self.publish_timestamp
        return self.state_is_published and publish_timestamp <= timezone.now()