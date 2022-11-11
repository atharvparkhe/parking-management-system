from django.db import models
from base.models import *


class CustomerModel(BaseUser):
    points = models.IntegerField(default=0)
    def __str__(self):
        return self.email
