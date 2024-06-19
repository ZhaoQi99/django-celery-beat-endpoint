# Django Celery Beat Status
[![Python version](https://img.shields.io/pypi/pyversions/django-celery-beat-status.svg?logo=python)](https://pypi.python.org/pypi/django-celery-beat-status)
![PyPI - Versions from Framework Classifiers](https://img.shields.io/pypi/frameworkversions/django/django-celery-beat-status)
[![PyPI package](https://img.shields.io/pypi/v/django-celery-beat-status.svg)](https://pypi.python.org/pypi/django-celery-beat-status)
[![PyPI download](https://img.shields.io/pypi/dm/django-celery-beat-status.svg)](https://pypi.python.org/pypi/django-celery-beat-status)
[![GitHub](https://img.shields.io/github/license/ZhaoQi99/django-celery-beat-status)](https://github.com/ZhaoQi99/django-celery-beat-status/blob/main/LICENSE)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/ZhaoQi99/django-celery-beat-status)

A library that provides `status` and `tasks` HTTP API for Django Celery Beat.

Inspired by [vintasoftware/django-celerybeat-status](https://github.com/vintasoftware/django-celerybeat-status)

## Requirements
* Python 3.6+
* [Django](https://docs.djangoproject.com/)
* [Celery](https://docs.celeryq.dev/)

## Install
```shell
pip install django-celery-beat-status
✨🍰✨
```
Or you can use `pip install git+https://github.com/ZhaoQi99/django-celery-beat-status.git
` install latest version.

## Usage
### Quick start
Just edit `proj/celery.py`, and replace `Celery` with `AwareCelery`

```python
from django_celery_beat_status.celery import AwareCelery
app = AwareCelery("proj")
# Or
from django_celery_beat_status.celery import AwareCelery as Celery
app = Celery("proj")

```
### Settings
You can easily configure lower case setting by referring [Configuration and defaults](https://docs.celeryq.dev/en/stable/userguide/configuration.html).

Or you can use a `CELERY_` prefix uppercase setting and loading configuration from the Django settings module.

* beat_port / CELERY_BEAT_PORT - port for http server
    > Default: 8005
* http_server / CELERY_BEAT_HTTP_SERVER - HTTP server class
    > Default: "django_celery_beat_status.backends:HTTPServer"

### API
* /status
```json
{
  "status": "OK"
}
```

* /tasks
```json
[
  {
    "name": "proj.tasks.add",
    "task": "",
    "args": "()",
    "last_run_at": "2024-06-18 20:00:00",
    "schedule": "<freq: 1.00 minute>",
    "kwargs": "{}",
    "is_due": true,
    "next_excecution": "2024-06-18 20:00:10"
  }
]
```
## Roadmap
- [ ] Support more server backends, such as Tornado, Flask and FastAPI.

## License
[GNU General Public License v3.0](https://github.com/ZhaoQi99/django-celery-beat-status/blob/main/LICENSE)

## Author
* Qi Zhao([zhaoqi99@outlook.com](mailto:zhaoqi99@outlook.com))