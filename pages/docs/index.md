
# Project Simulation Example

This project was designed to simulate critical components of the proposed architecture.

## Components and Services

The simulation includes the following key components and services:

- **BFF API Example:** 

  - Provides a simplified backend-for-frontend interface tailored specifically for an application.
  - Generates mock responses representing results from hypothetical backend services.
  
- **Pub/Sub to BigQuery Sink:**

  - Simulates the ingestion pipeline, transferring GPS coordinates published by the application into a BigQuery landing layer.

- **Infra as code:**
  - Code executed locally for managing resources at GCP

- **Github Actions**
  - Simulates minimum CD for building API image and deployments on GKE

## Dataset Simulation

The provided dataset simulates realistic GPS coordinates for vehicles traveling along routes between selected cities. Each GPS record contains the following data:

- **Timestamp** indicating when the GPS coordinate was captured.
- **Latitude and Longitude** representing vehicle location.
- Clearly defined **Start and End Coordinates** for each trip.
- **Car ID**
- **City ID**
- **Trip ID**
- **User ID**
- **Driver ID**
- **Event ID**

### Simulation Details

- **Cities Included:**
  - San Francisco
  - Chicago
  - Seattle
  - New York
  - Los Angeles

- **Number of Cars Simulated:** 1,000
- **Total Number of Trips:** 5,000 (5 trips per car)
- **Average Duration per Trip:** 15 minutes

## Public endpoint sample

Accessible at [here](http://35.241.50.52/docs)

For local executions check the [README.md](../../src/README.md)
