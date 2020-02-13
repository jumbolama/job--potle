from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from job_app.models import Category
from job_app.models import Jobs
from .models import Jobs
from django.views import View
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)
# Create your views here.
class CategoryJobsView(View):
    def get(self, request, category_id, *args, **kwargs):
        template_name = "job/catagories.html"
        template_name= "index.html"
        # category = Category.objects.get(pk=category_id)
        category = get_object_or_404(Category, pk=category_id)
        category_Jobs_list = Jobs.objects.filter(category=category)
        return render(
            request, template_name, {"category_jobs_list": category_Jobs_list, "category": category}
        )
class JobsTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        catagories = Category.objects.all()
        print(catagories)
        category_jobs_list = {}
        for category in catagories:
            # context[category.title] = Jobs.objects.filter(category=category)
            category_jobs_list[category] = Jobs.objects.filter(category=category)
        context["jobs_list"] = Jobs.objects.all().order_by("-created_at")[:4]
        context["trending_job"] = Jobs.objects.order_by("-count")
        context["category_jobs_list"] = category_jobs_list
        print(context)
        return context
class JobsDetail(DetailView):
    model = Jobs
    template_name = "job/single_jobs.html"
    context_object_name = "detail_jobs"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        self.object.save()
        context["popular_jobs"] = Jobs.objects.order_by("-count")[:4]
        return context