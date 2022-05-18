from random import randint

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal

from accounts.factories import UserFactory
from references.factories import ReferenceFactory
from articles.models import Article


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    audience = randint(1, 999999)
    price = FuzzyDecimal(0.5, 100000, 2)
    reference = SubFactory(ReferenceFactory)
    user = SubFactory(UserFactory)
