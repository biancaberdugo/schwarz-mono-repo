# Case Taxi platform simulation

For general information please check out the official documentation page at https://biancaberdugo.github.io/schwarz-mono-repo/

BFF simulation API can be found [here](src/README.md)

Infra as code can be found [here](infrastructure/README.md)

## Project Simulation Example

This project was designed to simulate sampled components of the proposed architecture.

### Components and Services

The simulation includes the following key components and services:

- **BFF API Example:** 
  - Provides a simplified backend-for-frontend interface tailored specifically for an application.
  - Includes necessary infrastructure to deploy the BFF API into Kubernetes.
  - Generates mock responses representing results from hypothetical backend services.
  - Publishes simulated trip data to a Pub/Sub topic.

- **Pub/Sub to BigQuery Sink:**
  - Simulates the ingestion pipeline, transferring GPS coordinates published by the application into a BigQuery landing layer.

### Dataset Simulation

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

#### Simulation Details

- **Cities Included:**
  - San Francisco
  - Chicago
  - Seattle
  - New York
  - Los Angeles

- **Number of Cars Simulated:** 1,000
- **Total Number of Trips:** 5,000 (5 trips per car)
- **Average Duration per Trip:** 15 minutes

### Public endpoint sample

Accessible at http://35.241.50.52/docs

For local executions check the [README.md](../../src/README.md)
