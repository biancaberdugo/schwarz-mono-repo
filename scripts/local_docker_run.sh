#!/bin/bash

docker run -p 80:8080 \
  -v "$HOME/.config/gcloud:/gcloud" \
  -e GOOGLE_APPLICATION_CREDENTIALS="/gcloud/application_default_credentials.json" \
  -it test_docker
