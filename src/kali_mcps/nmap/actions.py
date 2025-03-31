import asyncio
from src.kali_mcps.base.kali_command import KaliCommand

class NmapCommand(KaliCommand):
    def __init__(self):
        super().__init__("nmap", 
                        network_enabled=True,  # nmap需要网络访问
                        memory_limit="2g",     # 需要更多内存
                        timeout=300)           # 需要更长的超时时间

async def basic_scan(target: str) -> tuple[str, str]:
    """
    Basic scan
    For example: nmap 192.168.1.1
    """
    cmd = NmapCommand()
    command = ["nmap", target]
    return await cmd.execute(command)

async def intense_scan(target: str) -> tuple[str, str]:
    """
    Intense scan (-T4 -A)
    Includes: OS detection, version detection, script scanning, and traceroute
    """
    cmd = NmapCommand()
    command = ["nmap", "-T4", "-A", target]
    return await cmd.execute(command)

async def stealth_scan(target: str) -> tuple[str, str]:
    """
    SYN scan (-sS)
    Half-open scan, more stealthy
    Requires root privileges
    """
    cmd = NmapCommand()
    command = ["nmap", "-sS", target]
    return await cmd.execute(command)

async def quick_scan(target: str) -> tuple[str, str]:
    """
    Quick scan (-T4 -F)
    Only scans the most common ports
    """
    cmd = NmapCommand()
    command = ["nmap", "-T4", "-F", target]
    return await cmd.execute(command)

async def vulnerability_scan(target: str) -> tuple[str, str]:
    """
    Vulnerability scan (-sV --script vuln)
    Uses vulnerability detection scripts
    """
    cmd = NmapCommand()
    command = ["nmap", "-sV", "--script", "vuln", target]
    return await cmd.execute(command)

if __name__ == "__main__":
    # Test example
    print(asyncio.run(quick_scan("10.1.1.106")))
