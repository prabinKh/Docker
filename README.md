# Docker

Dockerfile
dockerfile
Copy code
FROM node
WORKDIR /myapp
COPY . /myapp/
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]
Docker Image and Containers
Build Docker Image
bash
Copy code
docker build -t react-app .
Check Docker Images
bash
Copy code
docker images
Run Docker Container
bash
Copy code
docker run -p 3000:3000 react-app
Run Container in Detached Mode
bash
Copy code
docker run -d -p 3000:3000 react-app
Run Multiple Containers
bash
Copy code
docker run -d -p 3001:3000 react-app
docker run -d -p 3002:3000 react-app
Stop and Remove Containers
bash
Copy code
docker stop <container_name_or_id>
docker rm <container_name_or_id>
Remove Images
bash
Copy code
docker rmi <image_id>
Volume Management
Save Data in a Volume
bash
Copy code
docker run -it --rm -v myvolume:/myapp react-app
Check Volumes
bash
Copy code
docker volume ls
docker volume inspect myvolume
Mount Local Files
bash
Copy code
docker run -it -v /path/to/local/file:/myapp/requirement.txt --rm react-app
MySQL and Python in Docker
Connecting Containers
Pull the MySQL image:
bash
Copy code
docker pull mysql:latest
Run a MySQL container:
bash
Copy code
docker run -d --name mysqldb --env MYSQL_ROOT_PASSWORD=root --env MYSQL_DATABASE=userinfo mysql
Inspect the container to get its IP:
bash
Copy code
docker inspect mysqldb
Update your Python code with the container's IP:
python
Copy code
host = "172.17.0.2"
user = "root"
password = "root"
database = "userinfo"
Local and Dockerized Connection
For local MySQL:

python
Copy code
host = "host.docker.internal"
Docker Networking
Create a Network
bash
Copy code
docker network create my-net
Connect Containers
Run MySQL container in the network:
bash
Copy code
docker run -d --env MYSQL_ROOT_PASSWORD=root --env MYSQL_DATABASE=userinfo --name mysqldb --network my-net mysql
Update the Python container to connect using the container name:
python
Copy code
host = "mysqldb"
user = "root"
password = "root"
database = "userinfo"





