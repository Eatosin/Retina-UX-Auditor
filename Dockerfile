# 1. Base Image
FROM python:3.11-slim

# 2. System Setup (CRITICAL for OpenCV)
# We install the GL libraries needed for image processing
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3. Work Directory
WORKDIR /app

# 4. Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Code
COPY --chown=user . .

# 6. Create Non-Root User (Security)
RUN useradd -m -u 1000 user
RUN chown -R user:user /app

# 7. Switch User
USER user
ENV PATH="/home/user/.local/bin:$PATH"
ENV PYTHONPATH=/app

# 8. Run Entry Point
CMD ["python", "run.py"]
