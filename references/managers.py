from __future__ import annotations

from decimal import Decimal
from typing import Dict

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class ReferenceManager(models.Manager):
    def listing_by_type(self, kind: str, user: User) -> Dict[str, Decimal | int]:
        return self.filter(kind=type, article__user=user).aggregate(
            audience=Sum("article__audience", default=0),
            price=Sum("article__price", default=0),
        )
