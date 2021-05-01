from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
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


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()  # 만으로 장고는 알아서 render 함 templates(딱 이 위치 ) 에 404.html을,//

    # templates/ 안해줘도 되는건가?

    # page_kwarg = "bitch" ?page= 대신에 "?bitch="

    # 지금 이걸 읽고있으면 제일 위의 주석을 읽어라,

    # ===========================================================
    # ===========ListView--Classy CBV////// ccbv.co.uk 참고------
    # ===========================================================
    # ===========ClassBasedBoew VS FunctionBasedView-------------
    # ===========================================================
