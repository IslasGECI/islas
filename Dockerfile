FROM python:3
COPY . /workdir/
WORKDIR /workdir
RUN pip install --upgrade pip && pip install \
    black \
    flake8 \
    geci-test-tools \
    mutmut \
    mypy \
    pylint \
    pytest \
    pytest-cov