FROM python:3.10

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port 7860 (Required for Hugging Face Spaces)
EXPOSE 7860

# Command to run the application with gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
