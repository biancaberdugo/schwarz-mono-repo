# Project Setup & Usage Guide

## 🚀 Getting Started

### 1. Set Up Virtual Environment

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 2. Authenticate with Google Cloud

Ensure you have credentials that can publish **Pub/Sub** messages for simulation purposes.

1. Install the **Google Cloud SDK**:  
   👉 [Google Cloud SDK Installation Guide](https://cloud.google.com/sdk/docs/install)

2. Authenticate:
   ```bash
   gcloud auth application-default login
   ```

---

## 🧪 Local Development

### 1. Generate Environment Variables

Run the following script to generate your local `.env` file:

```bash
chmod +x scripts/stage_build_env_file.sh
sh scripts/stage_build_env_file.sh
```

### 2. Start the Application

Run the main script from the root directory:

```bash
python -m src.api.main
```

Alternatively, you can run it directly from your **PyCharm** environment for better debugging and project management.

### 3. Endpoints

#### Send Simulation Metrics to Pub/Sub
```
/api/v1/simulate-events/taxi-route/trip-coordinates/
```

Select a dataset from the list and each line will be emitted as an event to Pub/Sub.

#### Simulate Cross-Service Communication
```
/api/v1/trips/new
```

**Simulates** a flow receiving a DTO from the application, invokes an external service, and translates the result back into a DTO understandable by the app.

---

## ✅ Running Tests

### Unit Tests

```bash
pytest tests/unit
```

### Integration Tests

```bash
pytest tests/it
```

## ✅ Deployment

Automatically executed by merging the code to main branch. It builds the Docker image and deploy changes over GKE