# 📊 {{cookiecutter.project_name}} Job

Welcome to the {{cookiecutter.project_name}} Job! This project is designed to automate the preparation, training, and evaluation of machine learning models using Python scripts and Docker for easy deployment and execution.

## 🚀 Project Structure

The project consists of three main components:

1. **Data Preparation**: Download and prepare the dataset for training.
2. **Model Training**: Train a machine learning model based on the specified task.
3. **Model Evaluation**: Evaluate the model's performance using various metrics.

## 📂 Repository Structure

- `main.py`: The main entry point for executing the prepare, train, and evaluate commands.
- `tasks/`: Contains all tasks related to data preparation, training, and evaluation.
  - `tasks/prepare.py`: Prepares the dataset by downloading and processing it.
  - `tasks/train.py`: Trains the {{cookiecutter.project_name}} model using the prepared dataset.
  - `tasks/evaluate.py`: Evaluates the trained model's performance.
- `docker-compose.yml`: Manages the Docker services for each task.

## 🛠️ Setup Instructions

### Prerequisites

- Docker
- Python 3.8+

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd {{cookiecutter.project_slug}}-job
   ```

2. **Build the Docker image**:
   ```bash
   docker-compose build
   ```

### Running the Project

Choose a model to train. Currently, two models are available and can be set using the environment variable `MODEL_NAME`: `"linear_regression"` and `"xgboost_classifier"`.

1. **Prepare the Data**:
   ```bash
   docker-compose run {{cookiecutter.project_slug}}-job-prepare
   ```

2. **Train the Model**:
   ```bash
   docker-compose run {{cookiecutter.project_slug}}-job-train
   ```

3. **Evaluate the Model**:
   ```bash
   docker-compose run {{cookiecutter.project_slug}}-job-evaluate
   ```

## 📝 Model Details

- **Algorithms**: [XGBoost Classifier, Linear Regressor]
- **Data Handling**: Techniques such as SMOTE can be used to balance the dataset during the preparation phase.
- **Evaluation Metrics**: Common metrics like Accuracy, Precision, Recall, and F1 Score.

## 📈 Output

- **Model**: Saved as `model.ubj` or `model.pkl` in the specified cache directory.
- **Evaluation Plot**: Visualization of model performance (e.g., log loss or other metrics) saved for analysis.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## 📜 License

This project is licensed under the MIT License.

## 📨 Contact

For any questions or inquiries, please contact at [{{cookiecutter.user_email}}](mailto:{{cookiecutter.user_email}}).

---

Thank you for checking out the {{cookiecutter.project_name}} Project! 😊
