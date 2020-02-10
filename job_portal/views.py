from django.shortcuts import render
def home(request):
    templates_name ="index.html"
    content = {"name":"mahesh"}
    return render(request,templates_name,content)