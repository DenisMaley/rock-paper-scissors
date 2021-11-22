# Pull python 3 image
FROM python:3
# Create a work dir
WORKDIR /app
# Copy entire project into workdir
COPY . .
# Install all requirements
RUN python3 -m pip install --user --no-cache-dir -r requirements.txt
# Run our app
ENTRYPOINT ["python", "app.py"]