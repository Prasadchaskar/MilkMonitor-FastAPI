# Milk Quality Prediction API

This project is a FastAPI application that predicts the quality of milk based on various parameters. The model is trained using machine learning techniques and deployed as an API.

## Project Structure
![image](https://github.com/user-attachments/assets/5dc606a5-3875-4753-8fe2-252f33e29d70)


## Setup Instructions

### Prerequisites

- Python 3.9
- Docker

### Install Dependencies

1. Create and activate a virtual environment:

    ```sh
    python -m venv env
    On Windows, use `env\Scripts\activate`
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Running the Application
1. Change directory
   ```sh
   cd app
   ```
3. Run the FastAPI application:

    ```sh
    fastapi dev main.py
    ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

### Docker Setup

1. Build the Docker image:

    ```sh
    docker build -t milk_quality_api .
    ```

2. Run the Docker container:

    ```sh
    docker run -p 80:80 milk_quality_api
    ```

3. Access the API at `http://127.0.0.1/`.

## API Endpoints

- `GET /` - Health check endpoint.
- `POST /predict` - Predict the quality of milk.
  
  **Request Body:**
  ```json
  {
      "pH": 6.7,
      "Temperature": 20.5,
      "Taste": 1,
      "Odor": 1,
      "Fat": 0,
      "Turbidity": 1,
      "Color": 254
  }
## Response
```json
{
    "Milk Quality": "High"
}
```
## Model Training
The machine learning model was trained using the following features:
- pH
- Temperature
- Taste
- Odor
- Fat
- Turbidity
- Color

The Random Forest model was found to perform the best, and the feature importance chart is included in the Jupyter Notebook.
