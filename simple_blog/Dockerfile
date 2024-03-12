FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/


# RUN python manage.py makemigrations
# RUN python manage.py migrate



# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

