# BUILD FOR PRODUCTION!
# NOT READY YET

FROM nffdiogosilva/pytools

LABEL maintainer="Nuno Diogo da Silva <diogosilva.nuno@gmail.com>"

COPY requirements* /.

WORKDIR /usr/src/app

RUN pip install -r requirements.txt && \
    pip install -r requirements-dev.txt

RUN python manage.py migrate && \
    python manage.py check

CMD [ "python", "manage.py", "runserver" ]
