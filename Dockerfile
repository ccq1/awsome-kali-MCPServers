# build headless kali images, which is used for mcps
FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y kali-linux-headless && \  
    apt-get install -y \
        iputils-ping \
        net-tools \
        dnsutils \
    apt-get clean

CMD ["/bin/bash"]