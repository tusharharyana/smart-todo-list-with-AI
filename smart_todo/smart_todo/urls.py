from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo import views
from todo.views import TaskViewSet, ContextEntryViewSet, CategoryViewSet, ai_suggestions

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'contexts', ContextEntryViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/ai/suggest/', ai_suggestions),  # AI Suggestion Endpoint
    path("api/ai/recommend/", views.recommend_task, name="recommend_task"),

]
