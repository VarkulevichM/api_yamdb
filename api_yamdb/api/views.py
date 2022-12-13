from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from ..reviews.models import Review, Title
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [] # пока ничего, надо согласовать пермишны
    pagination_class = PageNumberPagination

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        return title.rewiews.all()
    
    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [] # пока ничего, надо согласовать пермишны
    pagination_class = PageNumberPagination

    def get_queryset(self):
        rewiew = get_object_or_404(
            Review,
            id=self.kwargs.get('rewiew_id')
        )
        return rewiew.comments.all()

    def perform_create(self, serializer):
        rewiew = get_object_or_404(
            Review,
            id=self.kwargs.get('rewiew_id')
        )
        serializer.save(author=self.request.user, rewiew=rewiew)
