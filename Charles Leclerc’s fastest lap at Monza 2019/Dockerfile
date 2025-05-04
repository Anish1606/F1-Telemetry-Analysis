FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies for matplotlib and OpenGL
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source files
COPY . .

# Run script
CMD ["python", "leclerc.py"]
