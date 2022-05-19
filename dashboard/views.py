from typing import Dict, Any, Mapping

from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from articles.models import Article
from references.models import Reference


class DashboardView(ListView):
    model = Article
    template_name = "dashboard/dashboard.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        return self.request.user.article_set.order_by("-created")

    def get_context_data(self, **kwargs: Mapping) -> Dict[str, Any]:
        """Add more context to dashboard as we want to display disks listing."""
        context = super().get_context_data(**kwargs)
        kinds = set(Reference.objects.values_list("kind", flat=True))
        context["models"] = {
            kind: Reference.objects.listing_by_kind(kind, self.request.user)
            for kind in kinds
        }
        catalog = Article.objects.get_revenue(user=self.request.user)
        context["total_audience"] = catalog["total_audience"]
        context["total_revenue"] = catalog["total_revenue"]
        return context


class CreateReferenceView(CreateView):
    model = Reference
    template_name = "dashboard/add.html"
    success_url = reverse_lazy("list-article")
    fields = ["label", "kind", "file"]


class CreateArticleView(CreateView):
    model = Article
    template_name = "dashboard/add.html"
    success_url = reverse_lazy("list-article")
    fields = ["audience", "price", "reference"]

    def form_valid(self, form) -> HttpResponseRedirect:
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteArticleView(DeleteView):
    model = Article
    template_name = "dashboard/delete.html"
    success_url = reverse_lazy("list-article")


class UpdateArticleView(UpdateView):
    model = Article
    template_name = "dashboard/update.html"
    success_url = reverse_lazy("list-article")
    fields = ["audience", "price", "reference"]
