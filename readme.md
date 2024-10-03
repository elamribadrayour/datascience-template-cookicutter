# Data Science Project Template

Welcome to the Data Science Project Template repository! This repository provides a Cookiecutter template to kickstart data science projects with a standardized structure, making it easier to manage and scale your work.

## 🎯 Features

- **Standardized Project Structure**: Organizes your code, data, and documentation in a consistent manner.
- **Flexible Configurations**: Easily customize project settings and dependencies.
- **Docker Integration**: Simplifies deployment and execution of your data science models.
- **FastAPI and Job Scripts**: Set up for both API deployment and job processing tasks.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.11+ installed on your system.

### Installation

1. **Install Cookiecutter**

   Cookiecutter is a command-line utility that creates projects from templates. Install it using pip:

   ```bash
   python3 -m pip install cookiecutter
   ```

### Create a New Project

To create a new data science project using this template, follow these steps:

1. **Run Cookiecutter**

   Execute the following command and follow the prompts to customize your project:

   ```bash
   python3 -m cookiecutter gh:elamribadrayour/cookiecutter-datascience-template
   ```

   Replace `gh:elamribadrayour/cookiecutter-datascience-template` with the appropriate repository URL or path if you are using a local template.

### Project Structure

Below is a typical structure for projects generated from this template:

```
my_project/
├── my_project-api/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── main.py
│   ├── requirements.txt
│   └── ...
├── my_project-cache/
│   └── ...
├── my_project-job/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── tasks/
│   └── ...
├── README.md
└── ...
```

## 🛠️ Usage

- **API Development**: Develop and deploy your models as APIs using FastAPI.
- **Job Processing**: Automate data preparation, training, and evaluation scripts.
- **Docker**: Use Docker to containerize your applications for consistent environments across development and production.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this template.

## 📜 License

This project is licensed under the MIT License.

## 📨 Contact

For any questions or feedback, please contact at [badrayour.elamr@protonmail.com](mailto:{{cookiecutter.user_email}}).

---

Thank you for using the Data Science Project Template! 😊
