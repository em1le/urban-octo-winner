from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from articles.managers import ArticleManager
from utils.models import LoggingModel


class Article(LoggingModel):

    price = models.FloatField(verbose_name=_("Prix"))

    audience = models.IntegerField(verbose_name=_("Audience"))

    reference = models.OneToOneField(
        "references.Reference",
        on_delete=models.SET_NULL,
        verbose_name=_("Référence")
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name=_("Utilisateur")
    )

    object = ArticleManager()

    def __str__(self) -> str:
        return f"{self.pk} | {self.reference}"
