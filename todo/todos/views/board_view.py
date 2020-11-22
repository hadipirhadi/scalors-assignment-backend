from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.board_model import Board
from ..serializers import BoardSerializer


class BoardView(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        """List all Boards"""
        response = super(BoardView, self).list(request, *args, **kwargs)
        return response

    def create(self, request, *args, **kwargs):
        """Crate a new Board"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 'success', 'pk': serializer.instance.pk})

    def partial_update(self, request, pk=None):
        """Handle Updating board title"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing Board"""

        return Response({'http_method': 'DELETE'})

    queryset = Board.objects.all()
    # serializer_class = BoardSerializer
    serializer_class = BoardSerializer
