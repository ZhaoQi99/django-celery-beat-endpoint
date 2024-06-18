from functools import cached_property

from celery import Celery


class AwareCelery(Celery):
    @cached_property
    def Beat(self, **kwargs):
        return self.subclass_with_self("django_celery_beat_status.beat:AwareBeat")
