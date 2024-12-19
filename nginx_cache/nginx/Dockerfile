# FROM nginx:latest

# RUN apt-get update && apt-get install -y procps

# RUN mkdir -p /home/app/staticfiles


FROM nginx:latest

RUN apt-get update && apt-get install -y procps

RUN mkdir -p /home/app/staticfiles /var/cache/nginx
# Copy static files from the build context
# COPY ../staticfiles /home/app/staticfiles