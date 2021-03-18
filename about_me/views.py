from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from .models import Courses, News
from .forms import MessForm


class ContextDataMixin:
    title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


def about(request):
    context = {'title': 'about me'}
    return render(request, 'about_me/index.html', context)


class StudiesView(ContextDataMixin, ListView):
    model = Courses
    template_name = 'about_me/curriculum.html'
    title = 'Curriculum'


def projects(request):
    context = {'title': 'projects'}
    return render(request, 'about_me/projects.html', context)


class NewsView(ContextDataMixin, ListView):
    model = News
    template_name = 'about_me/news.html'
    title = 'News'


class ContactsView(ContextDataMixin, CreateView):
    form_class = MessForm
    template_name = 'about_me/contacts.html'
    title = 'News'

# def contacts(request):
#     if request.method == 'POST':
#         date_from_form = MessForm(request.POST)
#         if date_from_form.is_valid():
#             date_from_form.save()
#             return redirect('contacts')
#     else:
#         date_from_form = MessForm()
#
#     context = {
#         'title': 'contacts',
#         'date_from_form': date_from_form
#     }
#
#     return render(request, 'about_me/contacts.html', context)
