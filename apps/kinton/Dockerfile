FROM resin/rpi-raspbian:jessie
# FROM debian:jessie

ENV KINTON_API_URL http://api.oclose.com
ENV KINTON_DIR /kinton

# Update system
RUN apt-get update && apt-get install -y wget supervisor python3-requests gettext

# Install Mosquitto
RUN wget -q -O - http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key | apt-key add -
RUN wget -q -O /etc/apt/sources.list.d/mosquitto-jessie.list http://repo.mosquitto.org/debian/mosquitto-jessie.list
RUN apt-get update && apt-get install -y mosquitto

# Add Mosquitto config
ADD config /kinton/config

# Add supervisor config
ADD supervisor/mosquitto.conf /etc/supervisor/conf.d/

# Volumes
VOLUME ["/kinton/data", "/kinton/logs"]

# Add scripts
ADD scripts/ /kinton/scripts

# Ports
EXPOSE 1884

ENTRYPOINT ["/kinton/scripts/entrypoint.sh"]
