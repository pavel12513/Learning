FROM centos

RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-*

RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*

RUN yum -y install openssh-server

RUN yum -y install passwd

RUN useradd remote_user && \
  echo "1234" | passwd remote_user --stdin && \
  mkdir /home/remote_user/.ssh && \
  chmod 700 /home/remote_user/.ssh 

COPY remote-key.pub /home/remote_user/.ssh/authorized_keys

RUN chown remote_user:remote_user -R /home/remote_user/.ssh/ && \
    chmod 600 /home/remote_user/.ssh/authorized_keys

RUN yum -y install epel-release && \
    yum -y install python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install awscli


RUN /usr/bin/ssh-keygen -A

EXPOSE 22

RUN rm -rf /run/nologin

CMD /usr/sbin/sshd -D
