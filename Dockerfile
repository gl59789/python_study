FROM python:3.7

ADD example001.py /
ADD syslog.log /

CMD [ "python3", "./example001.py" ]