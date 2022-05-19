from __future__ import annotations

from decimal import Decimal
from typing import Dict

from django.db import models


class ArticleManager(models.Manager):
    def get_revenue(self, user) -> Dict[str, Decimal | int]:
        catalog = {"total_revenue": 0, "total_audience": 0}
        for article in self.filter(user=user):
            catalog["total_revenue"] += article.total_revenue
            catalog["total_audience"] += article.audience
        return catalog

