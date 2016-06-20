#!/bin/bash

if [ -z "$KINTON_DIR" ]; then
  echo "Error: \"KINTON_DIR\" not defined"
  exit 1
fi

UUID_FILE="$KINTON_DIR/data/uuid"

if [ ! -f "$UUID_FILE" ]; then
    echo "Initializing registration process..."
    $KINTON_DIR/scripts/register.py
    if [ "$?" -gt "0" ]; then
      echo "Error on registration process"
      exit 1
    fi
  else
    echo "Hub already registered"
fi
export KINTON_UUID=$(head -n 1 $UUID_FILE)

echo "UUID: $KINTON_UUID"

envsubst < $KINTON_DIR/config/mosquitto/conf.d/kinton.template > $KINTON_DIR/config/mosquitto/conf.d/kinton.conf

# Start services
supervisord -n
