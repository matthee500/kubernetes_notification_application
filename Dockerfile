FROM python:3-alpine

# Create a non-root user
RUN adduser -D user_1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Change ownership of the /app directory to the non-root user
RUN chown -R user_1:user_1 /app

# Switch to the non-root user
USER user_1

# Run the application
CMD ["python", "main.py"]