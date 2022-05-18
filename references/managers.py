from typing import Dict

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class ReferenceManager(models.Manager):
    ...
