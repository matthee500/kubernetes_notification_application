# About
This application contains a Python script that checks the status and response time of a website and sends a message to a Discord channel. The script uses the `json`, `requests`, and `os` modules. The `get_status_and_response_time` function takes a hostname as input and returns the status code and response time of the website. The `send_discord_message` function takes a webhook URL and content as inputs and sends a message to a Discord channel. The main function checks the status and response time of a website and sends a message to a Discord channel using the `discord_url` variable. If run as a standalone program, the script runs the main function.

## How it works
The Python script is written to perform a specific task, such as scraping data from a website or sending a notification. The script is then packaged into a Docker image using a Dockerfile that specifies the base image, dependencies, and commands to run the script. The Docker image is pushed to a registry, such as Docker Hub or Google Container Registry, or even a local Docker registry where it can be accessed by Kubernetes. A Kubernetes cron job is created using a YAML file that defines the schedule, image name, resources, and environment variables for the container. The cron job runs the container at the specified time and terminates it when the script finishes.

## Guide
### Follow these steps to get an example application working:

1. Clone this repository to your system.
2. Get a Discord webhook URL and place it in the `discord_url` variable in the Python script.
3. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and enable Kubernetes.
Build the Docker image with either the latest tag or a specific tag. This tag will be used to push the image to a local or external container registry.
4. Tag the image for use on the container registry using the tag specified in the previous step. For example, to tag an image for use on a local registry: `docker tag exampleapplication:0.1 localhost:5000/exampleapplication:0.1` .
5. Push the container to the registry. For example, to push an image to a local registry: `docker push localhost:5000/exampleapplication:0.1` .
6. Run the Kubernetes deployment file: `kubectl apply -f kubernetes-script.yaml` .
7. The application will now send notifications on Discord on the schedule that was defined in the `kubernetes-script.yaml` file. If the time specified was `"*/30 * * * *"` a notification will be sent at minute 0 and minute 30 of every hour, 10:00 and 10:30 for example. 