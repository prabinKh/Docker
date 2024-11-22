FROM nginx:latest
COPY ./html/index.html /usr/share/nginx/html/index.html
RUN apt-get update && apt-get install -y procps
#docker build -t my-nginx-html .
#docker run -d -p 8080:80 my-nginx-html
# see runding post = > docker ps
#stopp running container => docker stop < container id>
#docker rm <container id>
# see image => docker images
#remove the image => docker rmi <image id>
#docker rmi -f 5723c46318c2

# RUN THE image => docker run -it a69fbd6e416b
# go instide  the container => docker run -it custom-nginx-image /bin/bash