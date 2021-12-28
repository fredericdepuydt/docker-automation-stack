FROM python:3.7
LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"

# installing requirements
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY scripts /usr/src/app

# Setting volume and workdir
VOLUME /usr/src/app/
WORKDIR /usr/src/app/
CMD python3 script.py