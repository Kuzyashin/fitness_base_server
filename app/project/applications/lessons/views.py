from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

# Create your views here.
from .models import Lesson
from .serializers import LessonSerializer


class LessonViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
