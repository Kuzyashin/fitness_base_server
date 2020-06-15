import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
application = get_wsgi_application()

from utils.amqp_handlers import PikaWorkerHandler, PikaProducerHandler
from lessons.models import Lesson
from lessons.utils.parser import get_data


producer = PikaProducerHandler(
    connection_string='amqp://guest:guest@localhost:5672/%2F',
    queue_name='lesson_ready_queue',
)


def callback(msg):
    lessons_data = get_data()
    Lesson.objects.all().delete()
    Lesson.objects.bulk_create(
        [
            Lesson(**lesson) for lesson in lessons_data
        ]
    )
    producer.publish_message(
        {"action": "ready", "channel_name": msg.get('channel_name')}
    )


worker = PikaWorkerHandler(
    connection_string='amqp://guest:guest@localhost:5672/%2F',
    callback=callback,
    main_queue_name='lesson_update_queue',
    consumer_tag='Worker#1'
)

worker.run_worker()