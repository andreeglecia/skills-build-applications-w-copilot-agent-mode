
import os
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet, api_root
from django.urls import path, include
from django.http import JsonResponse

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')


# Custom root view to show API base URL using $CODESPACE_NAME

def api_root_with_url(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        api_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        api_url = "http://localhost:8000/api/"
    endpoints = {
        "users": f"{api_url}users/",
        "teams": f"{api_url}teams/",
        "activities": f"{api_url}activities/",
        "workouts": f"{api_url}workouts/",
        "leaderboard": f"{api_url}leaderboard/"
    }
    return JsonResponse({
        "api_base_url": api_url,
        "endpoints": endpoints
    })

urlpatterns = [
    path('', api_root_with_url, name='api-root'),
    path('', include(router.urls)),
]
