# Use an official Python image as base
FROM python:3.9  

# Set the working directory inside the container
WORKDIR /app  

# Copy all files from the current directory to /app
COPY . /app  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  

# Expose port 5000 for Flask
EXPOSE 5000  

# Start the Flask app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
 
