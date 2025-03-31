import asyncio
import docker
import tarfile
import os
import io
from typing import Optional, Dict, Any
from dataclasses import dataclass

class SandboxSettings:
    """sandbox configuration settings"""
    def __init__(
        self,
        image: str = "ubuntu-systemd:22.04",
        memory_limit: str = "2g",
        cpu_limit: float = 1.0,
        network_enabled: bool = True,
        network_mode: str = "bridge",
        timeout: int = 300
    ):
        self.image = image
        self.memory_limit = memory_limit
        self.cpu_limit = cpu_limit
        self.network_enabled = network_enabled
        self.network_mode = network_mode
        self.timeout = timeout

class SandboxError(Exception):
    """Base exception for sandbox-related errors."""


class SandboxTimeoutError(SandboxError):
    """Exception raised when a sandbox operation times out."""


class SandboxResourceError(SandboxError):
    """Exception raised for resource-related errors."""


class SandboxClient:
    """Sandbox client, providing only container creation and cleanup functionality"""
    
    def __init__(self):
        self.client = docker.from_env()
        self.container = None

    async def create(self, config: SandboxSettings) -> None:
        """Create and start the container"""
        try:
            # prepare container configuration
            container_config = {
                "image": config.image,
                "detach": True,
                "mem_limit": config.memory_limit,
                "nano_cpus": int(config.cpu_limit * 1e9),
                "network_mode": config.network_mode if config.network_enabled else "none",
            }
            
            # create and start container
            self.container = self.client.containers.run(**container_config)
            print(f"Container created: {self.container.id}")
        except Exception as e:
            raise SandboxError(f"Failed to create container: {str(e)}")
    
    async def run_command(self, command: str) -> str:
        """Execute a command in the container"""
        if not self.container:
            raise SandboxError("Container not created")
        
        try:
            exec_result = self.container.exec_run(command, tty=True)
            return exec_result.output.decode('utf-8')
        except Exception as e:
            raise SandboxError(f"Failed to execute command: {str(e)}")

    async def copy_to_container(self, source_path: str, container_path: str) -> None:
        """
        Copy a file from host to container
        Args:
            source_path: Path to the file on host
            container_path: Path where to put the file in container
        """
        if not self.container:
            raise SandboxError("Container not created")
        
        try:
            # create a memory-based tar file
            tar_stream = io.BytesIO()
            with tarfile.open(fileobj=tar_stream, mode='w') as tar:
                # add file to tar
                tar.add(source_path, arcname=os.path.basename(container_path))
            
            tar_stream.seek(0)
            # copy to container
            self.container.put_archive(
                path=os.path.dirname(container_path),
                data=tar_stream
            )
            print(f"File copied to container: {container_path}")
        except Exception as e:
            raise SandboxError(f"Failed to copy file to container: {str(e)}")

    async def copy_from_container(self, container_path: str, dest_path: str) -> None:
        """
        Copy a file from container to host
        Args:
            container_path: Path to the file in container
            dest_path: Path where to put the file on host
        """
        if not self.container:
            raise SandboxError("Container not created")
        
        try:
            # get the tar stream of the file from container
            bits, stat = self.container.get_archive(container_path)
            
            # create the destination directory (if it doesn't exist)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            # write the tar stream to a temporary file
            with open(dest_path, 'wb') as f:
                for chunk in bits:
                    f.write(chunk)
            print(f"File copied from container: {dest_path}")
        except Exception as e:
            raise SandboxError(f"Failed to copy file from container: {str(e)}")
    
    async def cleanup(self) -> None:
        """Clean up and remove the container"""
        if self.container:
            try:
                self.container.stop()
                self.container.remove()
                print(f"Container cleaned up: {self.container.id}")
                self.container = None
            except Exception as e:
                print(f"Error cleaning up container: {str(e)}")

def create_sandbox_client() -> SandboxClient:
    """Create a factory function for the sandbox client"""
    return SandboxClient()



# example
async def run_in_sandbox(command: str) -> str:
    """Run a command in the sandbox"""
    config = SandboxSettings()
    client = create_sandbox_client()
    
    try:
        await client.create(config=config)
        result = await client.run_command(command)
        return result
    except SandboxTimeoutError:
        return "Command execution timed out"
    except SandboxError as e:
        return f"Sandbox execution error: {str(e)}"
    except Exception as e:
        return f"Unknown error: {str(e)}"
    finally:
        await client.cleanup()

# if you run this script directly
if __name__ == "__main__":
    async def main():
        print("Starting sandbox test...")

        result = await run_in_sandbox("echo 'Sandbox test successful'")
        print(result)
    
    asyncio.run(main()) 