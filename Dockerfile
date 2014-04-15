FROM ubuntu:12.10
MAINTAINER Nicholas Lippis "nicholas.lippis@gmail.com"
RUN apt-get -qq update
RUN apt-get install -y python-dev python-setuptools supervisor git-core
RUN easy_install pip
RUN pip install virtualenv
RUN pip install uwsgi
RUN virtualenv --no-site-packages /opt/ve/layup
ADD . /opt/apps/layup
ADD .docker/supervisor.conf /opt/supervisor.conf
ADD .docker/run.sh /usr/local/bin/run
RUN (cd /opt/apps/layup && git remote rm origin)
RUN (cd /opt/apps/layup && git remote add origin https://github.com/nlippis/layup.git)
RUN /opt/ve/layup/bin/pip install -r /opt/apps/layup/requirements.txt
RUN (cd /opt/apps/layup && /opt/ve/layup/bin/python manage.py syncdb --noinput)
RUN (cd /opt/apps/layup && /opt/ve/layup/bin/python manage.py collectstatic --noinput)
EXPOSE 8000
CMD ["/bin/sh", "-e", "/usr/local/bin/run"]
