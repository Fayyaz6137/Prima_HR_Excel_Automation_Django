from django.urls import path
from .views import upload_page, history_page, download_output

urlpatterns = [
    path('', upload_page, name='upload'),
    path('history/', history_page, name='history'),
    path('media/outputs/<str:filename>/', download_output, name='download_output'),

]
