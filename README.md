## End to End Machine Learning Project

This repository contains an end-to-end machine learning project for student performance prediction. The project is organized into several folders and files as described below:

### Project Structure

```
mlproject/
│
├── README.md                # Project overview and instructions
├── requirements.txt         # Python dependencies
├── setup.py                 # Project installation script
├── setup_env.sh             # Shell script to set up the environment
├── app.py                   # Flask web application entry point
│
├── logs/                    # Log files generated during runs
│   └── <timestamp>.log/     # Log folders by run timestamp
│       └── <timestamp>.log  # Log file for a specific run
│
├── mlproject.egg-info/      # Metadata for the installed package
│   └── ...                  # (Auto-generated files)
│
├── notebook/                # Jupyter notebooks for EDA and model training
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb   # Exploratory Data Analysis
│   ├── 2. MODEL TRAINING.ipynb              # Model training steps
│   └── data/
│       └── stud.csv         # Dataset used in the project
│
├── src/                     # Source code for the project
│   ├── __init__.py
│   ├── exception.py         # Custom exception handling
│   ├── logger.py            # Logging utility
│   ├── utils.py             # Utility functions
│   ├── components/          # Core ML pipeline components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py        # Data ingestion logic
│   │   ├── data_transformation.py   # Data transformation logic
│   │   └── model_trainer.py         # Model training logic
│   └── pipeline/            # Pipeline scripts
│       ├── __init__.py
│       ├── predict_pipeline.py      # Prediction pipeline
│       └── train_pipeline.py        # Training pipeline
```

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd mlproject
   ```
2. **Set up the environment:**
   ```bash
   bash setup_env.sh
   ```
3. **Activate the conda environment:**
   ```bash
   conda activate my__env
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run notebooks:**
   Open the notebooks in the `notebook/` folder for EDA and model training.

### Folder Descriptions

- **logs/**: Contains log files for each run, organized by timestamp.
- **mlproject.egg-info/**: Metadata generated after installing the package.
- **notebook/**: Jupyter notebooks for EDA and model training, as well as CatBoost training artifacts and the dataset.
- **src/**: All source code, including exception handling, logging, utilities, ML pipeline components, and pipeline scripts.
  - **components/data_ingestion.py**: Handles the process of reading raw data, splitting it into training and test sets, and saving the processed data for further steps in the machine learning pipeline.
  - **components/data_transformation.py**: Responsible for transforming raw data into a suitable format for model training, including preprocessing steps such as encoding, scaling, and feature engineering.
  - **components/model_trainer.py**: Contains the logic for training machine learning models, selecting the best model, and saving the trained model artifact.
  - **pipeline/predict_pipeline.py**: Contains the `PredictPipeline` class for generating predictions using the trained model and preprocessing pipeline, and the `CustomData` class for collecting and formatting user input data (from the Flask web form) into a DataFrame suitable for prediction. This enables integration with the Flask app and the HTML form in `templates/home.html` for real-time predictions.
  - **utils.py**: Includes utility functions, such as model evaluation, to assess the performance of trained models using metrics like R2 score and more.
  - **main.py**: The main entry point for running the project pipeline or application logic.
  - **app.py**: The Flask web application entry point. Handles HTTP requests, renders HTML templates, collects user input, and serves real-time predictions using the trained model pipeline.

### License

This project is for educational purposes.