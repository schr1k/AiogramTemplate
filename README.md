# Setup

1. Install dependencies.
    ```bash
    uv sync
    ```

2. Install pre-commit to automatically lint and format via ruff before commit
    ```bash
    uv run pre-commit install
    ```

3. Copy and modify .env
    ```bash
    cp .env.example .env
    ```

# Launch

### Docker

* Development mode (fast-refresh)
    ```bash
    docker compose watch
    ```

* Production mode
    ```bash
    docker compose up --build -d
    ```

### Pure python
* Development mode
    ```bash
    uv run main.py
    ```

* Production mode
    ```bash
    uv run --no-dev main.py
    ```