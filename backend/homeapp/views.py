# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Strategy
from .serializers import StrategySerializer

class StrategyList(APIView):
    """
    List all strategies, or create a new strategy.
    """

    def get(self, request, format=None):
        strategies = Strategy.objects.all()
        serializer = StrategySerializer(strategies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StrategySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
