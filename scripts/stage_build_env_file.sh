#!/bin/bash

# Store here any type of credential key to be fetched from a secret manager
# This script should simulate by loading the secrets into env vars for local and testing purposes
# On stage and production, those secrets will be mapped by the usage of Kubernetes External secrets

# E.g.:
# temporal_secrets=$(gcloud secrets versions access latest --secret=${TEMPORAL_SECRET_NAME})
# TEMPORAL_CERTIFICATE="$(printf "%s" "$temporal_secrets" | jq -r '.TEMPORAL_CERTIFICATE')"


# Create .env directory if it doesn't exist
mkdir -p src/api/.env

# Define the environment variables
cat <<EOL > src/api/.env/.local.env
ENV="local"
CLOUD="GCP"
VERSION="0.0.1"
SERVICE="BFF API Taxi Service"
TEAM="schwarz_data_platform"
PUBSUB__PROJECT_ID="decisive-cinema-296013"
TAXI_ROUTE_TOPIC_ID="route-metrics-topic"
EVENTS_STREAMING_TYPE="PUBSUB"
EOL

# Define the environment variables
cat <<EOL > src/api/.env/.unittest.env
ENV="unit"
CLOUD="GCP"
VERSION="0.0.1"
SERVICE="BFF API Taxi Service"
TEAM="schwarz_data_platform"
MOCK__PROJECT_ID="mock"
TAXI_ROUTE_TOPIC_ID="mock"
EVENTS_STREAMING_TYPE="MOCK"
EOL

# Confirm creation
echo ".local.env file has been created in the .env directory."