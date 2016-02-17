FROM ubuntu:latest

ENV SRVHOME /srv/dockerexample
ENV DIP 172.16.5.146

COPY . ${SRVHOME}

WORKDIR ${SRVHOME}

RUN apt-get update && apt-get -y install libpq-dev nodejs npm python python-dev python-pip

RUN npm install -g bower && \
    pip install -r requirements.txt

RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN python manage.py bower install -- --allow-root && \
    python manage.py migrate


VOLUME ["/static"]

EXPOSE 80

# Only for example we would use nginx or apache for real
CMD ["/srv/dockerexample/runserver.sh"]
