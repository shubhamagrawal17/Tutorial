# --- Stage 1: Builder ---
# This stage installs compilers and build tools to compile dependencies
FROM python:3.11-slim AS builder

WORKDIR /build

# Prevents Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .

# Install dependencies into a local folder (wheels)
RUN pip install --no-cache-dir --user -r requirements.txt


# --- Stage 2: Final Runtime ---
# This stage is tiny and contains only the application and its runtime
FROM python:3.11-slim AS runtime

WORKDIR /app

# Create a non-privileged user for security
# if an attacker breaks into your app, 
# they are trapped as a 'standard user' rather than having 'root' access.
RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -s /bin/bash appuser

# Copy only the installed dependencies from the builder stage
COPY --from=builder /root/.local /home/appuser/.local
COPY app app

# Ensure the app user owns the application directory
RUN chown -R appuser:appuser /app

# Set PATH to include the local user bin (where uvicorn is)
ENV PATH=/home/appuser/.local/bin:$PATH

# Switch to the non-root user
USER appuser

EXPOSE 8000

# Use a production-grade uvicorn configuration
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]