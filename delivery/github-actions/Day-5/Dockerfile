FROM python:3.11-slim

WORKDIR /app

# ✅ Copy only requirements first (better caching)
COPY requirements.txt .

# ✅ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Now copy application code
COPY app ./app

# (optional) If you have other files like .env or configs
# COPY .env .

# ✅ Expose port (not mandatory but good practice)
EXPOSE 8000

# ✅ Start app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]