# CSC325 Django CI/CD Project

**Author:** Carlos Gonzalez  
**Course:** CSC325, Module 8 (CI/CD with GitHub Actions)

A small Django + Django REST Framework backend with an automated CI/CD pipeline. Every push to `main` installs the project, runs the test suite, and only deploys if all tests pass.

## Links
- **Live API:** https://csc325djangoproject.onrender.com/api/hello/
- **Pipeline runs:** [Actions tab](https://github.com/carlosgonzal100/CSC325DjangoProject/actions)

> Hosted on Render's free tier. The first load may take up to a minute while the server wakes up.

## Endpoints
| URL | Type | Returns |
|---|---|---|
| `/` | Django view | HTML home page |
| `/about/` | Django view | HTML about page |
| `/api/hello/` | DRF API (GET) | JSON response |

Example response from `/api/hello/`:
```json
{
  "message": "Hello from the CSC325 Django API",
  "course": "CSC325",
  "student": "Carlos Gonzalez"
}
```

## CI/CD Pipeline
Workflow file: [`.github/workflows/csc325_ci_cd.yml`](.github/workflows/csc325_ci_cd.yml)

Runs automatically on every **push to `main`**. Its stages, in order:

| Stage | What it does |
|---|---|
| **Setup** | Checks out the code and installs Python 3.12 |
| **Dependencies** | Installs packages from `requirements.txt` |
| **Test** | Runs the full test suite with `python manage.py test` |
| **Deploy** | Runs only after Test passes |

The steps run in order, so if any test fails the job stops and Deploy never runs. Render is set to auto-deploy only after the GitHub checks pass, so broken code never goes live.

## Tests
10 tests in [`myapp/tests.py`](myapp/tests.py) check:
- the home and about pages load and show the correct text
- each URL is connected to the correct view
- an unknown page returns a 404
- the `/api/hello/` endpoint returns status 200 and the correct JSON fields (`message`, `course`, `student`)

## Branching
- `main` is protected by a ruleset that blocks deletions and force pushes.
- New work is done on a feature branch (for example `feature/add_student`) and then merged into `main`.

## Run Locally
```bash
git clone https://github.com/carlosgonzal100/CSC325DjangoProject.git
cd CSC325DjangoProject
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py test
python manage.py runserver
```
Then open http://127.0.0.1:8000/api/hello/

## Tech Stack
Python 3.12 · Django · Django REST Framework · Gunicorn · GitHub Actions · Render

## Credits
Built by following the CSC325 Module 8 tutorial, with assistance from Claude (Anthropic) for debugging the workflow, writing tests, and setting up deployment.
