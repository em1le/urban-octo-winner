from django.db import models
from django.utils.translation import gettext_lazy as _

from references.managers import ReferenceManager
from utils.models import LoggingModel


class ReferenceKind(models.TextChoices):
    VIDEO = "video", _("Vidéo")
    AUDIO = "audio", _("Audio")
    PHOTO = "photo", _("Photo")
    MISC = "misc", _("Divers")


class Reference(LoggingModel):

    label = models.CharField(verbose_name=_("Label"), max_length=80)

    kind = models.CharField(
        verbose_name=_("Type"),
        max_length=5,
        choices=ReferenceKind.choices,
        default=ReferenceKind.VIDEO,
    )

    file = models.FileField(verbose_name=_("Fichier"), upload_to="media/")

    objects = ReferenceManager()

    def __str__(self) -> str:
        return f"{self.kind} | {self.label}"

    class Meta:
        verbose_name = _("Référence")
        verbose_name_plural = _("Références")
