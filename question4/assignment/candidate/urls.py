from django.urls import path, re_path
from .views import add_candidate, add_score,get_best, get_avg,creating_user


urlpatterns = [
    path("add/", add_candidate),
    path("add_score/", add_score),
    path("best/", get_best),
    path("avg/",get_avg),
    path("signup/", creating_user),
    

]
