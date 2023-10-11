from django.urls import path
from bank.views import AccountView, IndexView, SendView, TrackView

app_name = "bank"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("account/<int:id>", AccountView.as_view(), name="account"),
    path("send", SendView.as_view(), name="send"),
    path("track", TrackView.as_view(), name="track"),
]