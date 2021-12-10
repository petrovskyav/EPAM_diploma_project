FROM centos

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt .
COPY entrypoint.sh .
COPY weather_collector ./weather_collector
RUN yum install -y python3 python3-pip
RUN /usr/bin/pip3 install --upgrade pip
RUN /usr/bin/pip3 install -r requirements.txt
EXPOSE 8000
#CMD ["gunicorn", "-b", "0.0.0.0:8000", "--workers=5", "weather_collector.wsgi", "--chdir", "weather_collector/"]
CMD ["python3", "weather_collector/manage.py", "runserver", "0.0.0.0:8000"]
