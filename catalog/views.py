from django.shortcuts import render, redirect


def index(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name}, {phone},{message}")
        return redirect('index')
    else:
        return render(request, 'catalog/contacts.html')


