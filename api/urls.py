from django.urls import path

from api.views import criterion
from api.views import project_criteria
from api.views import project
from api.views import category

urlpatterns = [
    path('criteria/', criterion.CriterionList.as_view()),
    path('criteria/<int:pk>', criterion.CriterionDetail.as_view()),
    path('categories/', category.CategoryList.as_view()),
    path('categories/<int:pk>', category.CategoryDetail.as_view()),
    path('projects/', project.ProjectList.as_view()),
    path('projects/<int:pk>', project.ProjectDetail.as_view()),
    path('project_criteria/', project_criteria.ProjectCriteriaList.as_view()),
    path('project_criteria/<int:pk>', project_criteria.ProjectCriteriaDetail.as_view()),
]
