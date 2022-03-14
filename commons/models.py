import uuid
from django.db import models

# Create your models here.

class BaseModel(models.Model):
  class Meta: 
    abstract = True

  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # deleted_at = models.DateTimeField(null=True)