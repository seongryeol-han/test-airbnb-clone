from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):
    # ListView 는 자동적으로  template 을 찾는다 -->Rooms 앱이니까 ,room_list !!!!!!!!!!!!!!
    # 지금 이걸 읽고있으면 바로 위의 주석을 읽어라,
    """HomeView Definition"""

    # ListView 는 아래 를 자동으로 -->object_list 함 --> room_list 에서 바로 object_list 사용
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "rooms"  # object_list -> rooms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RoomDatail(DetailView):

    """RoomDatail Definition"""

    # DetailView ---> arg 로 정확히 pk 가 와야함.
    # 잘못도니값 --> 알아서 Not Found 페이지로 보내 벌임
    model = models.Room
    pk_url_kwarg = "potato"
    # pk-->potato

    # templates/ 안해줘도 되는건가?

    # page_kwarg = "bitch" ?page= 대신에 "?bitch="

    # 지금 이걸 읽고있으면 제일 위의 주석을 읽어라,

    # ===========================================================
    # ===========ListView--Classy CBV////// ccbv.co.uk 참고------
    # ===========================================================
    # ===========ClassBasedBoew VS FunctionBasedView-------------
    # ===========================================================
