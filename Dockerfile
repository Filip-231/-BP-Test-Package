FROM python:3.9-slim
RUN useradd --create-home --shell /bin/bash app_user
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update
COPY . .
RUN pip install -e .
CMD ["bash"]
