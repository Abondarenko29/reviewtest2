from django.urls import path
from .views import review_list, add_review

urlpatterns = [
    path("", review_list, name="review-list"),
    path("add/", add_review, name="add-review"),
]
