
from django.test import TestCase

from references.models import Reference
from articles.factories import ArticleFactory


class ReferenceTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.article = ArticleFactory()
        super().setUpTestData()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_listing_by_model(self):
        expected = {"audience": self.article.audience, "price": self.article.price}
        reference_kind = self.article.reference.kind
        result = Reference.objects.listing_by_kind(reference_kind, self.article.user)
        self.assertDictEqual(result, expected)
