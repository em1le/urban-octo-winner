from decimal import Decimal
from random import randint

from factory import SubFactory
from factory.django import DjangoModelFactory

from accounts.factories import UserFactory
from references.factories import ReferenceFactory
from articles.models import Article


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    audience = randint(1, 1000000)
    price = Decimal(randint(1, 10000))
    reference = SubFactory(ReferenceFactory)
    user = SubFactory(UserFactory)
