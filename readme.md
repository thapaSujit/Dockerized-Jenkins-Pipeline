# Installation
## Build the Jenkins BlueOcean Docker Image (or pull and use the one I built)
```
docker build -t myjenkins-blueocean:2.414.2 .
```

## Create the network 'jenkins'
```
docker network create jenkins
```

## Run the Container
### Windows
```
ddocker run --name my-jenkins-build --restart=on-failure --detach `
   --network jenkins --env DOCKER_HOST=tcp://docker:2376 `
   --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
   --volume jenkins-data:/var/jenkins_home `
   --volume jenkins-docker-certs:/certs/client:ro `
   --publish 8080:8080 --publish 50000:50000 my-jenkins-build:1.0 
```


## Get the Password
```
docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword
```

## Connect to the Jenkins
```
https://localhost:8080/
```

## Installation Reference:
https://www.jenkins.io/doc/book/installing/docker/

## Setting up alpine/socat Container for Jenkins-Docker Integration

To enable communication between Jenkins running as a container and Docker Desktop on the host machine, we use an Alpine/socat container to forward traffic. This setup allows us to run Jenkins on top of Docker while simultaneously using Docker as a cloud agent.

- Docker Host Configuration

1. When running Jenkins as a container, specify the unix or tcp address of the Docker host in the Docker host URI field.

   - Note: The Jenkins container cannot directly reach the Docker host's unix port.

- Socat Container Setup

2. Run an additional container to mediate between the Docker host and the Jenkins container. This container will expose the Docker host's unix port as its tcp port.

   - Follow the instructions in the [alpine/socat container documentation](https://hub.docker.com/r/alpine/socat/) to create the socat container.

- Jenkins Docker Configuration

3. After creating the socat container, update the Docker configuration in Jenkins.

   - Set the Docker host URI to `tcp://socat-container-ip:2375`.

- Test Connection

4. Run a test connection in the Jenkins Docker configuration.

   - The connection should now succeed, allowing seamless communication between Jenkins and Docker Desktop on the host machine.

5. Details can be found in following links 

https://stackoverflow.com/questions/47709208/how-to-find-docker-host-uri-to-be-used-in-jenkins-docker-plugin
```
docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
docker inspect <container_id> | grep IPAddress
```

## Using my Jenkins Python Agent
```
docker pull devopsjourney1/myjenkinsagents:python
```
## Acknowledgments

I would like to express my gratitude to DevOps Journey for creating an incredibly helpful video that greatly assisted me in understanding Jenkins.

[Link to the Helpful Video](https://www.youtube.com/watch?v=6YZvp2GwT0A)