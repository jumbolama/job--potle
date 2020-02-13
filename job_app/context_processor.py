from django.shortcuts import render
from job_app.models import Category


def categories(request):
    category_list = Category.objects.all()
    return {"categories": category_list}