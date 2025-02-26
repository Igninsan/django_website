from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

first_salary = 20000
second_salary = 50000
third_salary = 100000


class ExperienceSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            if experience < 1:
                return HttpResponseBadRequest('Для получения работы нужен 1 год опыта работы')
            elif experience >= 1 and experience <= 4:
                request.salary = first_salary
            elif experience >= 5 and experience <= 9:
                request.salary = second_salary
            elif experience >= 10 and experience <= 40:
                request.salary = third_salary
            else:
                return HttpResponseBadRequest('Вы слишком стары для получения этой работы')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'salary', 'заработная плата не определена')