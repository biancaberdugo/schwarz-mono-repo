#!/bin/bash

# Remove existing credentials
rm -rf /Users/bianca.berdugo/.config/gcloud/application_default_credentials.json

# Revoke all current gcloud auth sessions
gcloud auth revoke --all

# Log in with gcloud
gcloud auth login

# Set the desired project
gcloud config set project decisive-cinema-296013

# Log in for Application Default Credentials
gcloud auth application-default login
