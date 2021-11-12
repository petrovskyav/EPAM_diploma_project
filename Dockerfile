FROM centos

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt weather_collector/ /usr/src/app/
RUN yum install -y python3 python3-pip
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN /usr/bin/pip3 install --upgrade pip
RUN /usr/bin/pip3 install -r requirements.txt
EXPOSE 80
