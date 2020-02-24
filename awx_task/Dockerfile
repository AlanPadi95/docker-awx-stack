FROM ansible/awx_task

USER root
RUN sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
RUN sudo pip install logstash
RUN sudo pip install python3-logstash