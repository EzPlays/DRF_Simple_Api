from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSelealizer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSelealizer

