import os
import logging
import subprocess


logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def add_dependencies(
    directory: str, dependencies: list, ci_dependencies: list = None
) -> None:
    """Add dependencies to a project's pyproject.toml in the specified directory."""
    logging.info(f"Adding dependencies to {directory}")

    # Change to the specified directory
    original_directory = os.getcwd()
    os.chdir(directory)

    try:
        # Add main dependencies
        for dep in dependencies:
            logging.info(f"Adding dependency: {dep}")
            subprocess.run(["poetry", "add", dep], check=True)

        # Add development dependencies if any
        if ci_dependencies:
            for dep in ci_dependencies:
                logging.info(f"Adding development dependency: {dep}")
                subprocess.run(["poetry", "add", dep, "--group", "ci"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred while adding dependencies: {e}")
    finally:
        # Change back to the original directory
        os.chdir(original_directory)


def configure_api_project():
    logging.info("Configuring API project")
    api_dependencies = [
        "numpy@1.26.4",
        "pandas",
        "orjson",
        "xgboost",
        "pydantic",
        "scikit-learn",
        "fastapi[standard]",  # Correctly formatted
    ]

    api_ci_dependencies = [
        "pytest",
        "ruff",
        "mypy",
        "pandas-stubs",
    ]

    add_dependencies(
        directory="{{cookiecutter.project_slug}}-api",
        dependencies=api_dependencies,
        ci_dependencies=api_ci_dependencies,
    )


def configure_job_project():
    logging.info("Configuring Job project")
    job_dependencies = [
        "numpy@1.26.4",
        "pandas",
        "xgboost",
        "scikit-learn",
        "shap",
        "typer",
        "requests",
        "pyarrow",
        "matplotlib",
        "imbalanced-learn",
        "joblib",
        "kaggle"
    ]

    job_ci_dependencies = [
        "pytest",
        "mypy",
        "ruff",
        "pandas-stubs",
        "types-shapely",
        "types-requests",
    ]

    add_dependencies(
        directory="{{cookiecutter.project_slug}}-job",
        dependencies=job_dependencies,
        ci_dependencies=job_ci_dependencies,
    )


def run() -> None:
    logging.info("Running post-generation script")
    if os.path.exists("{{cookiecutter.project_slug}}-api"):
        configure_api_project()

    if os.path.exists("{{cookiecutter.project_slug}}-job"):
        configure_job_project()

    logging.info("Post-generation script completed")


if __name__ == "__main__":
    run()
