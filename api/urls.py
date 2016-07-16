"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include, patterns
from rest_framework import routers
from api.steady.views.user_view import UserView
from api.steady.views.prompt_view import PromptView
from api.steady.views.entry_view import EntryView
from api.steady.views.scoresheet_view import ScoreSheetView

from api.steady import provided_views as views

router = routers.DefaultRouter()
router.register(r'steady_users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [url(r'^', include(router.urls)),
               url(r'^prompts', PromptView.as_view()),
               url(r'^users', UserView.as_view()),
               url(r'^entries', EntryView.as_view()),
               url(r'^scoresheets', ScoreSheetView.as_view()), url(
                   r'^api-auth/',
                   include('rest_framework.urls',
                           namespace='rest_framework'))]
