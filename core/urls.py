from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
# room_views.HomeView.as_view : 함수가 와야함 !! 클래스 XXXXXXXroom_views.HomeViewXXXXXXXX
