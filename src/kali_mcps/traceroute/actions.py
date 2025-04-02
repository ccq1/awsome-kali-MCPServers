import asyncio
from src.kali_mcps.base.kali_command import CommandRunner

class TracerouteCommand(CommandRunner):
    def __init__(self):
        super().__init__("traceroute", network_enabled=True, memory_limit="1g", timeout=120)

def traceroute_action(target: str):
    """
    Traceroute to the target
    """
    cmd = TracerouteCommand()
    command = ["traceroute", target]
    return cmd.execute(command)


if __name__ == "__main__":
    print(traceroute_action("8.8.8.8"))