from django.shortcuts import render


def ping(request):
    return render(request, 'ping.html')


def pong(request):
    context = {
        'user_name': request.GET.get('name'),
        'user_age': request.GET.get('age'),
    }
    return render(request, 'pong.html', context)


def post_ping(request):
    return render(request, 'post_ping.html')


def post_pong(request):
    context = {
        'username': request.POST.get('username'),
        'password': request.POST.get('password'),
    }
    return render(request, 'post_pong.html', context)


def static_example(request):
    return render(request, 'static_example.html')
