from django.urls import path

from api.views import criterion

urlpatterns = [
    path('criteria/', criterion.CriterionList.as_view()),
    path('criteria/<int:pk>', criterion.CriterionDetail.as_view()),
]
