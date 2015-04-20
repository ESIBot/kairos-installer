# Kairos Installer

This repository contains the required components to get **Kairos Hub** running
on a Rapsberry Pi. There are multiple installation methods:

1. Using [resin.io](http://resin.io) image to get an out-of-the-box
  Kairos installation.
2. Using Kairos Docker image
3. Running the installation script on your current Raspbian installation.

## Use resin.io image

Everything should work out of the box.

## Kairos Docker images

Docker is required.

```bash
docker run esibot/kairos
```

## Installation script

Docker is required for Kinton installation. The following components will be installed on your system:

- Kinton Docker image
  - Mosquitto
  - Kinton auth service
- Kairos RF24 Gatway
- Kairos Kinton module
