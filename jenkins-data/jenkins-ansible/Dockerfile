FROM jenkins/jenkins
USER root

RUN apt-get update && \
    apt-get -y install python3 && apt-get -y install ansible

USER jenkins