from django.shortcuts import render, redirect
from . import models, forms
from django.views.generic import ListView, FormView

# PARSER FILM LIST
class TsListView(ListView):
    template_name = 'parser_app/ts_list.html'
    context_object_name = 'ts'
    model = models.TsModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class RezkaListView(ListView):
    template_name = 'parser_app/rezka_list.html'
    context_object_name = 'rezka'
    model = models.RezkaModel


    def get_queryset(self):
        return self.model.objects.all().order_by('id')


# PARSER FORMS
class TsFormView(FormView):
    template_name = 'parser_app/ts_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect('ts_list')
        else:
            return super(TsFormView, self).post(request, *args, **kwargs)


class RezkaFormView(FormView):
    template_name = 'parser_app/ts_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect('rezka_list')
        else:
            return super(RezkaFormView, self).post(request, *args, **kwargs)