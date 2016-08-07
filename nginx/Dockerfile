FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-available/default
ADD default /etc/nginx/sites-available/

EXPOSE 80

CMD ["/usr/sbin/nginx"]