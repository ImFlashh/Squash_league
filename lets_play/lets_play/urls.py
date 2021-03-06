"""lets_play URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lets_play_app.views import SignUpView, HomeView, ShowProfileView, CreateReservationView,\
    SportCenterDetailView, SportCenterListView, JoinRoomView, ReservationDetailView, DeleteRoom,\
    UserReservationsView, UserHistoryView, EditProfileView, UserFutureGamesView, MessagesView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^profile/(?P<user_id>[0-9]+)$', ShowProfileView.as_view(), name='profile'),
    url(r'^create_reservation/$', CreateReservationView.as_view(), name='create_reservation'),
    url(r'^sport_center/(?P<slug>[\w-]+)$', SportCenterDetailView.as_view(), name='sp_detail'),
    url(r'^sport_centres/$', SportCenterListView.as_view(), name='create_room'),
    url(r'^reservations_list/$', JoinRoomView.as_view(), name='reservations_list'),
    url(r'^reservations_list/(?P<room_id>[\d]+)$', ReservationDetailView.as_view(), name='room'),
    url(r'^delete_room/(?P<room_id>[\d]+)$', DeleteRoom.as_view(), name='delete_room'),
    url(r'^user_reservations/$', UserReservationsView.as_view(), name='user_reservations'),
    url(r'^user_history/$', UserHistoryView.as_view(), name='user_history'),
    url(r'^user_games/$', UserFutureGamesView.as_view(), name='user_games'),
    url(r'^edit_profile/$', EditProfileView.as_view(), name='edit_profile'),
    url(r'^messages/$', MessagesView.as_view(), name='messages'),
    # url(r'^calendar/$', MessagesView.as_view(), name='messages'),

    #reset password
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
