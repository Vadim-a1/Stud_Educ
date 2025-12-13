from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    ##return render(request, 'textbook/index.html')
    return render(request, 'textbook/index.html')

def lectures(request):
    return render(request, 'textbook/lectures.html')

def tests(request):
    return render(request, 'textbook/tests.html')


def lab(request):
    return render(request, 'textbook/lab.html')

LECTURES = {
    1: {
        'title': 'Экспертные системы',
        'pdf': 'lectures/1.pdf',
    },
    2: {
        'title': 'СТРУКТУРА И ФУНКЦИОНИРОВАНИЕ ЭКСПЕРТНЫХ  СИСТЕМ',
        'pdf': 'lectures/2.pdf',
    },
    3: {
        'title': 'ПРЕДСТАВЛЕНИЕ ЗНАНИЙ',
        'pdf': 'lectures/3.pdf',
    },
    4: {
        'title': 'ИНСТРУМЕНТАЛЬНАЯ ЭКСПЕРТНАЯ СИСТЕМА ExPRO 2 ',
        'pdf': 'lectures/14.pdf',
    },
    5: {
        'title': 'ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ',
        'pdf': 'lectures/5.pdf',
    },
    6: {
        'title': 'ИДЕНТИФИКАЦИЯ ЗАДАЧИ ОБРАБОТКИ  ИНФОРМАЦИИ И УПРАВЛЕНИЯ',
        'pdf': 'lectures/lab1.pdf',
    },
    7: {
        'title': ' МЕТОДЫ ПРИОБРЕТЕНИЯ ЗНАНИЙ. МЕТОДЫ ПОСТРОЕНИЯ МОДЕЛИ ПРЕДМЕТНОЙ ОБЛАСТИ. СЕМАНТИЧЕСКИЕ СЕТИ',
        'pdf': 'lectures/lab2.pdf',
    },
    8: {
        'title': 'МЕХАНИЗМ ЛОГИЧЕСКОГО ВЫВОДА  В ЭС ПРОДУКЦИОННОГО ТИПА',
        'pdf': 'lectures/lab3.pdf',
    },
    9: {   
        'title': 'ИНСТРУМЕНТАЛЬНЫЕ  СРЕДСТВА РАЗРАБОТКИ ЭС',
        'pdf': 'lectures/lab4.pdf',
    },
    
    
}

def lecture_detail(request, lecture_id):
    lecture = LECTURES.get(lecture_id)
    if not lecture:
        return render(request, '404.html', status=404)

    return render(request, 'textbook/lecture_detail.html', {
        'lecture': lecture
    })

