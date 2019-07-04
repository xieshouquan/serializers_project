from django.urls import path

from serializer_lesson.views import ProductCategoryView, UserView

urlpatterns=[
    path("category/",ProductCategoryView.as_view()),
    path("category/<slug:pk>/",ProductCategoryView.as_view()),
    path("user/",UserView.as_view()),
    path("user/<slug:pk>/",UserView.as_view()),
    # path("digui/<slug:pk>/",DiGui.as_view()),
]