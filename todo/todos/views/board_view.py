from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models.board_model import Board
from ..serializers import BoardSerializer
    #, NameSerializer


class BoardView(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        """List all Boards"""
        queryset = Board.objects.all()
        serializer = BoardSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Crate a new Board"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 'success', 'pk': serializer.instance.pk})

    def partial_update(self, request, pk=None):
        """Handle Updating board title"""
        queryset = Board.objects.filter(pk=pk)
        serializer = NameSerializer(queryset)
        if serializer.is_valid():
            serializer.save()
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing Board"""
        queryset = Board.objects.Delete(pk=pk)
        # serializer_class = BoardSerializer
        serializer = BoardSerializer(queryset)
        return Response({'http_method': 'DELETE'})


class BoardList(ListCreateAPIView):

    serializer_class = BoardSerializer
    permission_classes = {permissions.IsAuthenticated,}

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)


class BoardDetail(RetrieveUpdateDestroyAPIView):

    serializer_class = BoardSerializer
    permission_classes = {permissions.IsAuthenticated,}
    lookup_field = "id"

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)
