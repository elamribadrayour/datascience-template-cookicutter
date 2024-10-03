import re


def check_project_name() -> None:
    # This regex allows any character in the project slug
    PROJECT_REGEX = r"^.+$"

    project_slug = "{{ cookiecutter.project_slug }}"

    if not re.match(PROJECT_REGEX, project_slug):
        raise ValueError(f"ERROR: The project slug ({project_slug}) is not valid!")


def run() -> None:
    check_project_name()


if __name__ == "__main__":
    run()
