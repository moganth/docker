import subprocess
import requests

# Run any docker command via subprocess
def run_command(command: list):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"output": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.strip()}

# Get image details from Docker Hub
def get_image_details(image_name: str, tag: str = "latest"):
    try:
        if '/' not in image_name:
            image_name = f'library/{image_name}'  # official images

        url = f"https://hub.docker.com/v2/repositories/{image_name}/tags/{tag}/"
        response = requests.get(url)

        if response.status_code == 200:
            return {"message": "Image found", "details": response.json()}
        elif response.status_code == 404:
            return {"error": "Image or tag not found"}
        else:
            return {"error": f"Unexpected error: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

# Run a Docker container
def run_container(image_name: str, container_name: str = None):
    command = ["docker", "run", "-d"]
    if container_name:
        command += ["--name", container_name]
    command.append(image_name)
    return run_command(command)

# List Docker containers
def list_containers(all_containers: bool = False):
    command = ["docker", "ps"]
    if all_containers:
        command.append("-a")
    return run_command(command)

# Get logs of a Docker container
def get_logs(container_name: str):
    return run_command(["docker", "logs", container_name])

# Delete a Docker container
def delete_container(container_name: str):
    return run_command(["docker", "rm", "-f", container_name])

# Create a Docker volume
def create_volume(volume_name: str):
    return run_command(["docker", "volume", "create", volume_name])

# List all Docker volumes
def list_volumes():
    return run_command(["docker", "volume", "ls"])

# Remove a Docker volume
def remove_volume(volume_name: str):
    return run_command(["docker", "volume", "rm", volume_name])
