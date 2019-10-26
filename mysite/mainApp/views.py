from django.shortcuts import render

def index(request):
        return render(request, 'mainApp/homePage.html')


def  contact(request):
        return render(request, 'mainApp/basic.html', {'content': ['ЕСЛИ У ВАС ЕСТЬ КАКИЕ-НИБУДЬ ВОПРОСЫ ПИШИТЕ', 'https://vk.com/id432426376']} )
