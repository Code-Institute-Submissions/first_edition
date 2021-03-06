from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name="view_bag"),
    path('add/<item_id>', views.add_to_bag, name="add_to_bag"),
    path('add/bag/<item_id>', views.add_to_bag, name="add_to_bag"),
    path(
        'add_to_saved/<item_id>', views.add_to_save_for_later, name="add_to_save_for_later"),
    path('adjust/<item_id>', views.adjust_bag, name="adjust_bag"),
    path('remove/<item_id>', views.remove_from_bag, name="remove_from_bag"),
    path(
        'remove_from_saved/<item_id>', views.remove_from_saved, name="remove_from_saved"),
    path(
        'remove_from_saved_no_toast/<item_id>', views.remove_from_saved_no_toast, name="removed_from_saved_no_toast"),
        ]
