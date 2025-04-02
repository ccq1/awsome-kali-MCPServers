FROM python:3.12-slim-bookworm

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        iputils-ping \
        net-tools \
        dnsutils \
        nmap \
        binutils \
        traceroute \
        tshark && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 


COPY . .

ENV PYTHONPATH=/app
ENV IS_SAFE=false

# set run cmd
ENTRYPOINT ["python", "app.py"]