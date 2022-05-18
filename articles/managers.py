from __future__ import annotations

from decimal import Decimal
from typing import Dict

from django.db import models


class ArticleManager(models.Manager):
    def get_catalog(self, user) -> Dict[str, Decimal | int]:
        catalog = {"price": 0, "audience": 0}
        for article in self.filter(user=user):
            catalog["price"] += article.price
            catalog["audience"] += article.audience
        return catalog

