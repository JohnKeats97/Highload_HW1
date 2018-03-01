FROM ubuntu:16.04

RUN apt-get -y update
RUN apt-get install -y python3

ADD ./ /var/www/html/

EXPOSE 80

CMD python3 /var/www/html/httpd.py --root /var/www/html
