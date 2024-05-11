# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import long_running_task

class StartLongRunningTask(APIView):
    def post(self, request):
        long_running_task.delay()
        return Response("Long running task started.", status=status.HTTP_200_OK)
