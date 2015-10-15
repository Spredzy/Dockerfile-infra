FROM spredzy:infra-base

RUN yum -y install openssh-server; yum clean all; systemctl enable sshd.service
RUN echo root:root | chpasswd && ssh-keygen -b 2048 -t rsa -f ~/.ssh/id_rsa -N ''

EXPOSE 22

CMD ["/usr/sbin/init"]
