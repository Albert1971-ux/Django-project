from django.http import HttpResponse

def data_view(request):
    return HttpResponse("<h1>Страница DATA</h1><p>Привет всем</p>")

def test_view(request):
    return HttpResponse("<h1>Страница TEST</h1><p>Здесь что-то для теста.</p>")

