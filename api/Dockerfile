FROM python:2.7

RUN pip install -U pipenv

WORKDIR /code
ADD . /code

RUN pipenv install --system
ENV FLASK_DEBUG=1
ENV FLASK_APP=app.py
ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD flask run --host=0.0.0.0
