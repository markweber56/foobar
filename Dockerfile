FROM base

USER root

COPY requirements.txt /home/main/requirements.txt

RUN pip install -r /home/main/requirements.txt
RUN chmod 755 /bin/bash

COPY . /home/main
RUN chown -R master:staff /home/main

VOLUME ./:/home/main/
USER master

ENV PYTHONPATH /home/main

ENTRYPOINT ["python3"]
