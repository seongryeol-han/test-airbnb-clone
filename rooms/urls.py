from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [path("<int:potato>", views.RoomDatail.as_view(), name="detail")]
