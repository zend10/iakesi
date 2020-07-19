from django.shortcuts import render


def submission(request):
    return render(request, 'base/submission.html')

def contact(request):
    return render(request, 'base/contact.html')

def about(request):
    return render(request, 'base/about.html')