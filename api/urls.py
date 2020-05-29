from django.urls import path

from api.views import criterion
from api.views import project_criteria
from api.views import project

urlpatterns = [
    path('criteria/', criterion.CriterionList.as_view()),
    path('criteria/<int:pk>', criterion.CriterionDetail.as_view()),
    path('projects/', project.ProjectList.as_view()),
    path('projects/<int:pk>', project.ProjectDetail.as_view()),
    path('project_criteria/', project_criteria.ProjectCriteriaList.as_view()),
    path('project_criteria/<int:pk>', project_criteria.ProjectCriteriaDetail.as_view()),
]
