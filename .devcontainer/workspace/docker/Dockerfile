FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN apt-get update -y \
  && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
  && pip install --upgrade pip \
  && pip install jupyterlab \
  && pip install qiskit \
  && pip install qiskit-ibm-runtime \
  && pip install 'qiskit[visualization]' \
  && pip install qiskit-aer-gpu \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/cache/apt/* /var/lib/apt/lists/
