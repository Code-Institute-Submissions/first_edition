from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path(
        "order_history/<order_number>", (
            views.order_history), name="order_history"),
    path("order_history", views.user_order_history, name="user_order_history")
]
