# actions-ci-lab

This repository is a teaching lab for **GitHub Actions** and the **software development lifecycle (SDLC)**.

The application is intentionally tiny: a Python function, `greet(name) -> str`, with pytest coverage of the happy path. The important part is the pipeline around it. Every push to `main`, and every pull request that targets `main`, starts a continuous integration (CI) workflow that installs the package and runs the tests. The goal is to see a change move from a branch, through a pull request, into an automated check before it is trusted on the default branch.

Repository: [Ashishkosana/actions-ci-lab](https://github.com/Ashishkosana/actions-ci-lab)

## What is in this repo

| Path | Role |
| --- | --- |
| `src/greeter/` | The package. `greet` lives in `src/greeter/__init__.py`. |
| `tests/test_greet.py` | Pytest tests for the happy path. |
| `pyproject.toml` | Package metadata and the pytest configuration. |
| `.github/workflows/ci.yml` | The CI workflow GitHub Actions runs. |

## What GitHub Actions is

**GitHub Actions** is GitHub's built-in automation platform. It runs commands in response to events in a repository, such as a push or a pull request.

**What it is used for:** in an SDLC, teams use it for continuous integration. Each change is checked out on a clean machine, dependencies are installed, and tests run automatically. A failing check is visible on the commit and on the pull request, so broken code is caught before it is merged.

## What a workflow is

A **workflow** is an automated process defined by a YAML file in `.github/workflows/`. This lab's workflow is [`.github/workflows/ci.yml`](.github/workflows/ci.yml). The `on:` block decides *when* it runs. The `jobs:` block decides *what* it does.

**What it is used for:** a workflow is the named pipeline you see in the Actions tab (here, **CI**). It is the unit you enable, disable, and re-run. This one exists to test the `greeter` package whenever code is pushed to `main` or proposed in a pull request against `main`.

## What a job is

A **job** is a group of steps that run on the same runner (a virtual machine). This workflow has one job, `test`, with `runs-on: ubuntu-latest`. Steps inside a job run in order and share the machine's filesystem. Separate jobs would get separate machines and would run in parallel unless you wire them together with `needs:`.

**What it is used for:** a job is one check on a commit or pull request. The `test` job is used to provide a Linux environment, put Python 3.12 on it, and run the test suite there. If any step in the job fails, the job fails, and the pull request check fails with it.

## What a step is

A **step** is a single task inside a job. A step either calls a reusable action with `uses:` or runs a shell command with `run:`.

This workflow has four steps, in order:

1. **Check out the repository** (`actions/checkout`) — copies this repo onto the runner. Later steps need the source files.
2. **Set up Python 3.12** (`actions/setup-python`) — installs the Python version the project requires.
3. **Install dependencies** — installs this package and pytest (`pip install -e ".[dev]"`).
4. **Run pytest** — executes the tests in `tests/`.

**What it is used for:** steps are the individual commands in the CI log. You open a failed step to see the exact output (a missing import, a failed assertion, and so on). Each step is used for one responsibility so a failure points at checkout, setup, install, or tests.

## How to open the Actions tab

1. Open [github.com/Ashishkosana/actions-ci-lab](https://github.com/Ashishkosana/actions-ci-lab).
2. Click the **Actions** tab.
3. In the left sidebar, select the **CI** workflow.
4. Open a run. You will see the **Run pytest** job, and under it the four steps with their logs.

A run appears for each push to `main` and for each pull request targeting `main`.

## How to open a pull request and see CI

1. Create a branch and change something small, such as the greeting text or a test.
2. Commit and push that branch to this repository.
3. Open a pull request whose base branch is `main`.
4. On the pull request, scroll to the checks near the merge box. **CI / Run pytest** should appear and then turn green or red.
5. Click **Details** next to that check to open the workflow run in the Actions tab.

That check is the SDLC gate for this lab: the pull request shows the proposed diff, and GitHub Actions shows whether the tests passed on a clean Ubuntu runner with Python 3.12.

## Run the tests locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

`pythonpath = ["src"]` in `pyproject.toml` also lets pytest import `greeter` without an editable install, which is useful while you are reading the tests. The CI job installs the package the same way a consumer would, then runs `pytest`.
