from django.urls import path, include

from .views import *

urlpatterns = [
    path("", chat_view, name="home"),
    path("chat/<username>", get_or_create_chatroom, name="start-chat"),
    path("chat/room/<chatroom_name>", chat_view, name="chatroom"),
    path("chat/fileupload/<chatroom_name>", chat_file_upload, name="chat-file-upload"),
]
