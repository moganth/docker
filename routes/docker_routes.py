from fastapi import APIRouter
from docker_utils import (
    get_image_details, run_container, list_containers,
    get_logs, delete_container, create_volume,
    list_volumes, remove_volume
)

router = APIRouter(prefix="/docker", tags=["Docker Commands"])

# Pull image details from Docker Hub
@router.get("/pull/{image_name}")
def pull_image_from_dockerhub(image_name: str, tag: str = "latest"):
    return get_image_details(image_name, tag)

# Run a Docker container
@router.post("/run/{image_name}")
def run(image_name: str, container_name: str = None):
    return run_container(image_name, container_name)

# List all Docker containers (including stopped ones)
@router.get("/ps")
def ps(all_containers: bool = True):
    return list_containers(all_containers=all_containers)

# Get logs from a Docker container
@router.get("/logs/{container_name}")
def logs(container_name: str):
    return get_logs(container_name)

# Delete a Docker container
@router.delete("/delete/{container_name}")
def delete(container_name: str):
    return delete_container(container_name)

# Create a Docker volume
@router.post("/volume/{volume_name}")
def create_volume_route(volume_name: str):
    return create_volume(volume_name)

# List all Docker volumes
@router.get("/volumes")
def get_volumes():
    return list_volumes()

# Remove a Docker volume
@router.delete("/volume/{volume_name}")
def delete_volume(volume_name: str):
    return remove_volume(volume_name)
