import nox

nox.options.sessions = ["format", "lint"]

@nox.session
def format(session):
    "Run formatters."
    session.install("-r", "requirements-test.txt")


@nox.session
def lint(session):
    "Run linters."
    session.install("-r", "requirements-test.txt")


@nox.session(name="check-deps")
def check_deps(session):
    "Check if the dependencies can be installed correctly."
    session.install("-r", "requirements-test.txt")
    session.run("pip", "list")
