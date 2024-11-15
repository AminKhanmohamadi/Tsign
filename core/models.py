from django.db import models

from core.validators import validate_file


# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=100 , db_index=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'folder'
        verbose_name_plural = 'folders'



class File(models.Model):
    TYPE_CHOICES = (
        ('image', 'image'),
        ('video', 'video'),
    )
    name = models.CharField(max_length=100 , db_index=True)
    file = models.FileField(upload_to='files' , validators=[validate_file])
    file_type = models.CharField(max_length=100,choices=TYPE_CHOICES , db_index=True)
    size = models.PositiveBigIntegerField(editable=False)
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE, null=True, blank=True , related_name='files')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.size = self.file.size
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'file'
        verbose_name_plural = 'files'
        unique_together = (('name', 'file_type'),)