from django.shortcuts import render


def home(request):
    context = {
        "message": "This is a boilerplate",
    }
    return render(request, "core/home.html", context)
