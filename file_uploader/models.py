from django.db import models
from news.models import Post

CATEGORY_CHOICES = (('regnskab', 'Regnskab'),
                    ('referat', 'Referat'),
                    ('andet', 'Andet'))

def get_upload_path(instance, filename):
    return '{category}/{filename}'.format(category=instance.category, filename=filename)

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    date = models.DateField()
    doc = models.FileField(upload_to=get_upload_path)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date',]

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
