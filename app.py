from src.mcp_server import mcp 
import argparse  # 添加 argparse 模块
import docker
from mcp.server.models import InitializationOptions


if __name__ == "__main__":
    # create arg parser
    parser = argparse.ArgumentParser(description='MCP Server with Kali image configuration')
    parser.add_argument('--kali-image', 
                       type=str,
                       required=False,
                       help='Specify the Kali Linux image name to use')
    
    args = parser.parse_args()
    if args.kali_image:
        image_name = args.kali_image
        # use docker lib to check if the image exists
        client = docker.from_env()
        try:
            client.images.get(image_name)
            print(f"Kali image {image_name} found")
            client.close()
        except docker.errors.ImageNotFound:
            print(f"Kali image {image_name} not found")
            exit(1)
        print(f"Using Kali image: {image_name}")
    
    print("Starting server is running")
    
    # pass image name to mcp
    mcp.run(transport="stdio")