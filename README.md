#Dockerfile for React Application
dockerfile
Copy code
FROM node  
WORKDIR /myapp  
COPY . /myapp/  
RUN npm install  
EXPOSE 3000  
CMD ["npm", "start"]  
##Docker Commands
#Create a Docker Image
bash
Copy code
docker build -t <image-name> .
Check Docker Images
bash
Copy code
docker images
# OR
docker images ls
Run the Image Inside a Container
bash
Copy code
docker run <image-id>
Check Running Containers
bash
Copy code
docker ps
Bind Container Port to Host Port
bash
Copy code
docker run -p 3000:3000 <image-id>
Run Docker Image in the Background
bash
Copy code
docker run -d -p 3000:3000 <image-id>
Run Multiple Containers from One Image
bash
Copy code
docker run -d -p 3001:3000 <image-id>
docker run -d -p 3002:3000 <image-id>
docker run -d -p 3004:3000 <image-id>
View All Containers (Running and Stopped)
bash
Copy code
docker ps -a
Delete a Container
bash
Copy code
docker rm <container-name>
Stop a Running Container
bash
Copy code
docker stop <container-name>
Automatically Delete Container After Stopping
bash
Copy code
docker run -d --rm -p 3000:3000 <image-id>
Name Containers and Images
Assign a Name to a Container
bash
Copy code
docker run -d --rm --name "prabin" -p 3001:3000 <image-id>
Tagging Images
bash
Copy code
docker build -t prabin:01 .
docker build -t prabin:02 .
Predefined Images
Use a Specific Node.js Version in Dockerfile
dockerfile
Copy code
FROM node:latest  # Or specify a version: node:14
Pull Other Images
bash
Copy code
docker pull python
docker pull nginx
Run an NGINX Container
bash
Copy code
docker run -p 8000:80 nginx:latest
# Access via: http://localhost:8000
Persistent Data and Volume Management
Save Data with Volumes
bash
Copy code
docker run -it --rm -v myvolume:/myapp <image-id>
-v indicates volume usage.
myvolume is the volume name.
/myapp is the working directory in the Docker container.
Check Volumes
bash
Copy code
docker volume ls
Inspect Volume Details
bash
Copy code
docker volume inspect myvolume
Mounting Local Files to Container
Mount a File
bash
Copy code
docker run -it -v /path/to/local/file:/container/path -rm <image-id>
Example:

bash
Copy code
docker run -it -v /User/root/Documents/pythonfilecontainer/requirement.txt:/myapp/requirement.txt -rm <image-id>
Connecting Two Containers (e.g., Python and MySQL)
Run a MySQL Container
bash
Copy code
docker pull mysql:latest
docker run -d --name mysqldb -e MYSQL_ROOT_PASSWORD="root" -e MYSQL_DATABASE="userinfo" mysql
Inspect MySQL Container for IP Address
bash
Copy code
docker inspect mysqldb
Use the IP address (e.g., 172.17.0.2) to connect in your Python code:

python
Copy code
host = "172.17.0.2"
user = "root"
password = "root"
database = "userinfo"
Local MySQL and Python Code in Containers
Use host.docker.internal as the MySQL host:

python
Copy code
host = "host.docker.internal"
user = "root"
password = "root"
database = "userinfo"
Docker Networking
Create a Docker Network
bash
Copy code
docker network create my-net
Run a MySQL Container on the Network
bash
Copy code
docker run -d --env MYSQL_DATABASE="userinfo" --env MYSQL_ROOT_PASSWORD="root" --name mysqldb --network my-net mysql
Update Python Code to Use MySQL Container Name as Host
python
Copy code
host = "mysqldb"
user = "root"
password = "root"
database = "userinfo"
