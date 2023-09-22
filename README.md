
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/csivitu/Template">
    <img src="https://csivit.com/images/favicon.png" alt="Logo" width="80">
  </a>

  <h3 align="center"><a name="lendlogic"></a>LendLogic</h3>
  <h4 align="center"><a name="the-crystal-ball-for-loans"></a>the crystal ball for loans 🔮</h4>
</p>

## Installation

To get started, follow these steps to set up your environment and install project dependencies:

```bash
# Clone the repository
git clone https://github.com/csivitu/LendLogic.git

# Navigate to the project directory
cd LendLogic

# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate

# Install project dependencies from requirements.txt
pip install -r requirements.txt
```
## Running Jupyter Notebook

To run Jupyter Notebook, use the following command:

```bash
jupyter notebook
```
This will start the Jupyter Notebook server, and you can access it in your web browser by following the provided URL.

## Running the Flask App

To run the Flask app, execute the following command:

```bash
python main.py
```
This will start the Flask development server, and your app will be accessible at `http://localhost:5000` in your web browser.

## Running a FastAPI Server and sending a Request to FastAPI

To run the FastAPI server, use the following command:

```bash
# Incase you are not in the FastAPI folder
cd FastAPI

# Run the Uvicorn server
uvicorn app:app --reload
```
This will start the FastAPI server, and your API will be accessible at `http://localhost:8000` in your web browser.

To send a request to the FastAPI server, you can use tools like `curl` or API client libraries like `requests`. Alternatively, you can use Postman, which is an application to test APIs utilizing a GUI.

