from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('curriculum/', views.StudiesView.as_view(), name='curriculum'),
    path('projects/', views.projects, name='projects'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('calculators/', include('calculators.urls', namespace='calculators')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)