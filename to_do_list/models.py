from django.db import models

from commons.models import BaseModel
from platform_auth.models import User

# Create your models here.


class ToDoListItem(BaseModel):
    class StatusEnum(models.TextChoices):
        TO_DO = ('TO_DO', 'To Do')
        IN_PROGRESS = ('IN_PROGRESS', 'In Progress')
        DONE = ('DONE', 'Done')
        PENDING = ('PENDING', 'Pending')
        TERMINATED = ('TERMINATED', 'Terminated')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField(default=StatusEnum.TO_DO,
                              choices=StatusEnum.choices)
    content = models.TextField()
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.uuid)
