# blog_web_project
Simple Blog Web App to study Python and Django

For that project I've used the following technologies:
- [Python 3.11.2](https://www.python.org/downloads/release/python-3104/)
- [Poetry](https://python-poetry.org/) modern and powerful package manager
- [Django](https://www.djangoproject.com/download/)
- [Postgres](https://www.postgresql.org/) main project database
- [Docker]() & [Docker Compose]() Containerized development tools
- [Pytest](https://docs.pytest.org/en/7.1.x/) modern, flexible python framework for testing
- [pre-commit](https://pre-commit.com/) additional version control tool

It's start of your journey on this project.
For convenience, I tried to use the features provided by containerization using `Docker` and
`Docker Compose`. They can greatly isolate the development process and unify the development result across all dev's
machines, but before using `Docker` you have to do a few steps:

**Install poetry package manager to your machine**
```shell
$ pip install poetry
```
**Activate poetry**
```shell
$ poetry shell
```
**Install dependencies to venv**
```shell
$ poetry install
```
## Launch application by `Docker`/`Docker Compose`
Firstly you need to create a `local.env` file in root directory. It can be empty, because by default,
Django uses standard Base URL. But, if you want to configure you custom URL, just add a new environment
variable `BASE_OFFER_MICROSERVICE_API` with your Base URL.

Next step is build Docker image:
#### Via `docker-compose`
```shell
$ docker-compose build
$ docker-compose up --no-start
$ docker-compose run --rm web python blog_web_project/manage.py migrate
$ docker-compose up
```

## Testing
To run the tests I also use the containerization provided by `Docker`.
#### Via `docker-compose`
```shell
$ docker-compose run --rm web pytest
```
after the tests pass, it is necessary to stop the work of containers.
```shell
$ docker-compose stop
```

## Additional tools
**pre-commit and other checkers (flake8, mypy, isort, black)**
> Before starting, you have to install the git hook scripts:
```shell
$ pre-commit install
```
Now pre-commit will run automatically on git commit, or you can
launch it manually:
```shell
$ pre-commit run --all-files
```
