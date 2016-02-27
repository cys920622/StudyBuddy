from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    course = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    preferred_location = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(editable=False)
    timestamp = models.DateTimeField(editable=False)
    # views = models.IntegerField() possible use later for counting number of times a post is viewed
    slug = models.SlugField(unique=True, editable=False)  # used for generating readable urls

    def __unicode__(self):
        return self.title

    # On save, update timestamp and updated and generate slug
    def save(self, *args, **kwargs):
        # only update timestamp when the object is first created
        # when id is not set yet
        if not self.id:
            self.timestamp = timezone.now()
        self.updated = timezone.now()
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)