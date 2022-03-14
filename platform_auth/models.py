from django.db import models
from django.contrib.auth import get_user_model

from commons.models import BaseModel

# this model is needed if need to custom the user data, without
# affecting the original user data from django
class User(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
