FROM nffdiogosilva/pytools

# Install git, process tools
RUN apt-get update && apt-get -y install git procps

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /workspace
WORKDIR /workspace

# Install Python dependencies from Pipfile
COPY requirements* /workspace/

RUN pip install -r requirements.txt && \
    pip install -r requirements-dev.txt