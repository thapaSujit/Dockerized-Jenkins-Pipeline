# Use the official Jenkins base image with JDK 11
FROM jenkins/jenkins:2.414.2-jdk11

# Switch to root user to perform system-level operations
USER root

# Update the package index and install necessary packages
RUN apt-get update && apt-get install -y lsb-release python3-pip

# Download the Docker GPG key for package verification
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg

# Configure Docker repository with the downloaded GPG key
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

# Update the package index again and install Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli

# Switch back to the Jenkins user for running Jenkins
USER jenkins

# Install specific Jenkins plugins using the jenkins-plugin-cli tool
RUN jenkins-plugin-cli --plugins "blueocean:1.25.3 docker-workflow:1.28"
