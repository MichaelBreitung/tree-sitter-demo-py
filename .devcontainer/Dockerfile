FROM ubuntu:22.04

# LABEL for the custom image
LABEL maintainer="michael.breitung@mibreit-photo.com"
LABEL version="0.1"
LABEL description="This is a custom Docker Image for Python Development."

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Setting bash as default shell
SHELL ["/bin/bash", "-c"]

# Update Ubuntu Software repository and install tools
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
  sudo=1.9.9-1ubuntu2.4 \
  iputils-ping=3:20211215-1 \
  git=1:2.34.1-1ubuntu1.11 \
  git-lfs=3.0.2-1ubuntu0.2 \
  python3=3.10.6-1~22.04.1 \
  python3-pip=22.0.2+dfsg-1ubuntu0.4 \
  ca-certificates=20240203~22.04.1 \
  curl=7.81.0-1ubuntu1.18 \
  openssh-server=1:8.9p1-3ubuntu0.10 \
  wget=1.21.2-2ubuntu1 \
  python3.10-venv \
  unzip=6.0-26ubuntu3.2 && \
  apt-get clean -y && \
  rm -rf /var/lib/apt/lists/*

# Install python packages
RUN pip3 install --no-cache-dir --upgrade \
  pip \
  pytest==8.3.2 \
  pytest-asyncio==0.24.0 \
  black==24.3.0 \
  pylint==3.1.0 \
  mypy==1.11.1 \
  requests==2.32.3 \
  sseclient==0.0.27

# Install Docker
RUN install -m 0755 -d /etc/apt/keyrings && \
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc && \
  chmod a+r /etc/apt/keyrings/docker.asc

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo $VERSION_CODENAME) stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null 
RUN apt update && apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# setup developer user
ENV UID=${UID:-1000}
ENV GID=${UID:-1000}
ENV USER=${USER:-developer}
RUN groupadd -g $GID $USER && \
  useradd -d /home/$USER -s /bin/bash -m $USER -l -u $UID -g $GID && \
  echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
  usermod -aG docker $USER
USER $USER

# Highlight Branch in Bash
RUN echo "parse_git_branch() {" >> ~/.bashrc && \
  echo "  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'" >> ~/.bashrc && \
  echo "}" >> ~/.bashrc && \
  echo "export PS1='\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ '" >> ~/.bashrc

# Update path
ENV PATH="$PATH:/home/developer/.local/bin"
