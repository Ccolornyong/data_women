from django.db import models
 
class AwardImageUpload(models.Model):
    title = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='about_me/awards/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updateed_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'