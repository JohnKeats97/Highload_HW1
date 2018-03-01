FROM ubuntu:16.04

USER root

RUN apt-get -y update
RUN apt-get install -y python3

EXPOSE 80

ADD ./ /var/www/html/
CMD python3 /var/www/html/httpd.py --root /var/www/html/
