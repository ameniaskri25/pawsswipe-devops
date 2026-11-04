# PawsSwipe DevOps — starter project

This project is the starting point for the Week 1–4 labs.

## Files in the starter
- `app.py`: Flask app, intentionally has no `/health` route at first.
- `requirements.txt`: Flask and Requests.
- `Dockerfile`: builds the container image.
- `.gitignore`: ignores virtual environments and Python cache files.

## Week 1 — run locally (Windows PowerShell)
1. Open this folder in VS Code.
2. In the terminal, run `python app.py`.
3. If Flask is missing, install dependencies: `python -m pip install flask requests`.
4. Set the environment variable in the same PowerShell terminal:
   `$env:DATABASE_URL="sqlite:///dummy.db"`
5. Run `python app.py` again and open `http://127.0.0.1:8080`.

For Windows CMD use:
`set DATABASE_URL=sqlite:///dummy.db`

## Week 2 — Docker
Run these commands from this folder:
1. `docker build -t pawsswipe:v2 .`
2. `docker run --rm -p 8080:8080 -e DATABASE_URL="sqlite:///docker_dummy.db" pawsswipe:v2`
3. Open `http://localhost:8080`.
4. In another terminal, check `docker ps`.

If port 8080 is already occupied, stop the other process/container or choose another host port, e.g. `-p 8081:8080`, then open `http://localhost:8081`.

## Week 3 — Git and GitHub
Run the Git commands from the lab sheet. The starter header is intentionally simple so you can edit it on `feature/cat-mode` and `main` to create the merge conflict.

## Week 4 — CI with GitHub Actions
The `week4_materials` folder contains the two files to add during Week 4:
- `test_app.py`
- `.github/workflows/ci.yml`

Copy them into the project root at the relevant Week 4 step. The first CI run is expected to fail because `/health` is not yet implemented. Then add the `/health` route to `app.py`, commit, and push again.

Add this line to `requirements.txt` during Week 4:
`pytest==7.4.0`

## Important
The app reads `DATABASE_URL` when `app.py` is imported. Set it before running the app or tests. The CI workflow sets it automatically.
