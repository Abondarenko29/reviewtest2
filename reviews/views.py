from django.shortcuts import render
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


def review_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(
        request,
        "reviews/review_list.html",
        context
    )


@login_required
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        Review.objects.create(form.save())
    else:
        form = ReviewForm()
        context = {"form": form}
        return render(request,
                      "reviews/add_review.html",
                      context)
