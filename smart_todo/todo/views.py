from rest_framework import viewsets
from .models import Task, ContextEntry, Category
from .serializers import TaskSerializer, ContextEntrySerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai_utils import suggest_task_features

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ContextEntryViewSet(viewsets.ModelViewSet):
    queryset = ContextEntry.objects.all()
    serializer_class = ContextEntrySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@api_view(['POST'])
def ai_suggestions(request):
    task_data = request.data.get('task', {})
    context_data = request.data.get('context', [])
    suggestions = suggest_task_features(task_data, context_data)
    return Response(suggestions)
