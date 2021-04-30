from django.contrib import admin
from django.utils.html import mark_safe  # get_thumbnail 의 html 이 먹히게 됨
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):  # admin.Stackedinlin : 형식이 다른거 기능 같음

    model = models.Photo  # Room 등록시에, 이미지 까지 같이 등록하기 위한 작업


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """RoomAdmin Admin Definition"""

    inlines = (PhotoInline,)  # Room 등록시에, 이미직 까지 같이 등록하기 위한작업

    fieldsets = (
        (
            "Basic info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Time", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About Space",
            {
                "classes": ("collapse",),  # 메뉴 숨김 선택창
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    ordering = ("name", "price")

    # 초기 메뉴바
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",  # 다대다 소겅은 못 옴
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    # 초기 메뉴바 우측 필터
    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    raw_id_fields = (
        "host",
    )  # 호스트를 검색할 수 있게 해줌 # 리스트가 아닌 선택창으로 변경의미 국가선택 에서 새로운 선택창 생각

    # 선택시 보이는 필드 설정
    # fields = ("country",)
    # exclude = ('country',) 반대
    # ^city : start with, =city : exactly
    # host__username : 외래키
    search_fields = ("=city", "host__username")

    filter_horizontal = (  # 다대다 관계에서 사용하는 것 !_!
        "amenities",
        "facilities",
        "house_rules",
    )

    # def save_model(self, request, obj, form, change):
    #    print(obj, change, form)
    #    super().save_model(request, obj, form, change)

    def count_amenities(self, obj):  # obj : 현재 row
        # print(obj) --> __str__ 출력
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """PhotoAdmin Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(
            f'<img src="{obj.file.url}", width=50px/>'
        )  # mark_safe import 한거임

    get_thumbnail.short_description = "thumbnail"
