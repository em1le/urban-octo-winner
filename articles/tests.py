from django.test import TestCase

from accounts.factories import UserFactory
from articles.factories import ArticleFactory
from articles.models import Article


class ArticleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.article = ArticleFactory(user=cls.user)
        super().setUpTestData()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_total_revenue(self):
        expected = self.article.price * self.article.audience
        result = self.article.total_revenue
        self.assertEqual(result, expected)

    def test_get_revenue(self):
        article2 = ArticleFactory(user=self.user)
        article3 = ArticleFactory(user=self.user)
        expected = {"total_audience": 0, "total_revenue": 0}
        for article in self.article, article2, article3:
            expected["total_audience"] += article.audience
            expected["total_revenue"] += article.total_revenue
        result = Article.objects.get_revenue(user=self.user)
        self.assertDictEqual(result, expected)
