import functools
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from articles.managers import ArticleManager
from utils.models import LoggingModel


class Article(LoggingModel):

    price = models.DecimalField(verbose_name=_("Prix"), decimal_places=2, max_digits=8)

    audience = models.IntegerField(verbose_name=_("Audience"))

    reference = models.OneToOneField(
        "references.Reference",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Référence"),
    )

    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name=_("Utilisateur")
    )

    objects = ArticleManager()

    def __str__(self) -> str:
        return f"{self.pk} | {self.reference}"

    @property
    @functools.lru_cache()
    def total_revenue(self) -> Decimal:
        return self.price * self.audience
