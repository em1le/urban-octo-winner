from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyChoice

from references.models import Reference, ReferenceKind


class ReferenceFactory(DjangoModelFactory):
    class Meta:
        model = Reference

    label = Faker("file_name")
    kind = FuzzyChoice(ReferenceKind.choices)
    file = Faker("url")
