import asyncio
from src.kali_mcps.base.kali_command import CommandRunner

class TracerouteCommand(CommandRunner):
    def __init__(self):
        super().__init__("traceroute", network_enabled=True, memory_limit="1g", timeout=120)

async def traceroute_action(target: str):
    """
    Traceroute to the target
    """
    cmd = TracerouteCommand()
    command = ["tracert", target]
    return await cmd.execute(command)


