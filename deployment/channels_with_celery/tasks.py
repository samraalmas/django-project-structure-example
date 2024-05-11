# tasks.py
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time

@shared_task
def long_running_task():
    channel_layer = get_channel_layer()
    for i in range(1, 11):
        intermediate_result = f"Intermediate result {i}"
        async_to_sync(channel_layer.group_send)(
            "intermediate_results",
            {
                "type": "send_intermediate_result",
                "result": intermediate_result
            }
        )
        time.sleep(10)  # Simulate processing time
    return "Task completed successfully"
