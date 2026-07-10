FROM python:3.13.14-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN addgroup --system --gid 10001 app \
    && adduser --system --uid 10001 --ingroup app --home /app app \
    && mkdir -p /app/staticfiles /app/media \
    && chown -R app:app /app

COPY requirements/base.txt /tmp/requirements.txt
RUN python -m pip install --requirement /tmp/requirements.txt

COPY --chown=app:app . /app

USER app

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--access-logfile", "-", "--error-logfile", "-"]
