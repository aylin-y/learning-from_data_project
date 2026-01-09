# Song Lyric Genre Classification

This project investigates the relationship between song lyrics and musical genres. By using machine learning models, the system attempts to predict the genre of a song based on its lyrical content. The workflow includes data collection via web scraping, text preprocessing, and a comparative analysis of different classification algorithms.

---

## Setup Instructions

Follow these steps to set up the environment and run the project locally.

### 1. Prerequisites

Ensure you have Python 3.9 or higher installed on your system. You will also need a Genius API Client Access Token. You can obtain one by creating an API application on the Genius Developers portal.

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies and avoid system-wide package conflicts.

**On macOS and Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate

```

### 3. Install Dependencies

Once the virtual environment is active, install the required libraries using the provided requirements file:

```bash
pip install -r requirements.txt

```

### 4. Configuration

The project uses environment variables to keep API keys secure. Create a file named `.env` in the root directory and add your Genius API token:

```text
GENIUS_API_KEY=your_token_here

```

---

## Project Structure

* **data_scraping_part1/2/3.py**: Scripts used to collect song lyrics from the Genius API.
* **LearningFromDataProject.ipynb**: The main Jupyter Notebook containing data cleaning, feature engineering, model training, and evaluation.
* **requirements.txt**: List of all Python libraries needed for the project.

---

## Usage

1. **Data Collection**: If you wish to expand the dataset, run the scraping scripts. Note that the notebook is designed to work with the existing CSV generated from these scripts.
2. **Model Training**: Launch the Jupyter Notebook to see the full analysis:
```bash
jupyter notebook LearningFromDataProject.ipynb

```
3. **Results**: The notebook compares Logistic Regression, Linear SVM, Random Forest, and MLP models based on accuracy, precision, and F1-score.
