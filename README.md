<h1 align="center">
  🎨📸 PhotoCircle
</h1>

## 🙌 Environment Setup

### 🐳 Needed tools

1. [Install Docker](https://www.docker.com/get-started)

### 🛠️ Environment configuration

1. Create a local environment file (`cp .env.template .env`)
2. If you want, you could modify any parameter

### 🔥 Application execution

1. Install all the dependencies and bring up the project with Docker executing: `./init.sh up --build`

### ✅ Tests execution

1. Install the dependencies if you haven't done it previously: `./init.sh -e test build`
2. Execute tests: `./init.sh -e test run --rm photo_api`

### 📝 API Docs

1. Run Server: `./init.sh up --build`
2. Go to website: `http://localhost:8080/docs`

## 👩‍🏫 Project explanation

## Utils

- Run command inside of docker: `make dev command=<command>`

- Run the migrations: `make migrate`

- Run Tests and Linters: `make test`

## External Links

### Technologies(Infrastructure)

- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [Sqlite](https://www.sqlite.org/index.html)
- [SQLAlchemy(ORM)](https://www.sqlalchemy.org/)
- [Palette Estimator](https://github.com/qTipTip/Pylette)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Local Storage](https://jowilf.github.io/sqlalchemy-file/)
