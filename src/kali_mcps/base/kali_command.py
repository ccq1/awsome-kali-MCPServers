import subprocess
import os
import asyncio
from src.sandbox import create_sandbox_client, SandboxSettings, SandboxTimeoutError, SandboxError

class CommandRunner:
    """Base class for executing Kali commands"""
    
    def __init__(self, command_name: str, network_enabled: bool = False, 
                 memory_limit: str = "1g", timeout: int = 120):
        """
        Initialize CommandRunner
        Args:
            command_name: Name of the command (e.g. 'objdump', 'nm', etc.)
            network_enabled: Whether network access is needed
            memory_limit: Memory limit for sandbox
            timeout: Timeout in seconds
        """
        self.command_name = command_name
        self.network_enabled = network_enabled
        self.memory_limit = memory_limit
        self.timeout = timeout
        self.IS_SAFE = os.environ.get("IS_SAFE", "false").lower() == "true"

    def run_command(self, command: list) -> tuple[str, str]:
        """Execute command and return output results"""
        try:
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            stdout, stderr = process.communicate()
            return stdout, stderr
        except Exception as e:
            return "", str(e)

    async def run_with_sandbox(self, command: list, input_files: dict = None) -> tuple[str, str]:
        """
        Execute command in Kali sandbox
        Args:
            command: Command to execute
            input_files: Dict of {local_path: container_path} for files to copy into container
        """
        kali_config = SandboxSettings(
            image="kalilinux/kali-rolling",
            memory_limit=self.memory_limit,
            cpu_limit=1.0,
            network_enabled=self.network_enabled,
            timeout=self.timeout
        )
        client = create_sandbox_client()
        try:
            await client.create(config=kali_config)
            
            # 如果有输入文件，先复制到容器中
            if input_files:
                for local_path, container_path in input_files.items():
                    await client.copy_to_container(local_path, container_path)
            
            # 执行命令
            cmd_str = " ".join(command)
            stdout = await client.run_command(cmd_str)
            return stdout, ""
        except Exception as e:
            return "", str(e)
        finally:
            await client.cleanup()

    async def safe_execute_kali_command(self, command: list, input_files: dict = None) -> tuple[str, str]:
        """
        Safely execute Kali command
        Args:
            command: Command to execute
            input_files: Dict of {local_path: container_path} for files to copy into container
        """
        try:
            result = await self.run_with_sandbox(command, input_files)
            return result
        except SandboxTimeoutError:
            return "", "Command execution timed out"
        except SandboxError as e:
            return "", f"Sandbox execution error: {str(e)}"
        except Exception as e:
            return "", f"Unknown error: {str(e)}"

    async def execute(self, command: list, input_files: dict = None) -> tuple[str, str]:
        """
        Execute command with safety check
        Args:
            command: Command to execute
            input_files: Dict of {local_path: container_path} for files to copy into container
        """
        if self.IS_SAFE:
            return await self.safe_execute_kali_command(command, input_files)
        else:
            return self.run_command(command)  