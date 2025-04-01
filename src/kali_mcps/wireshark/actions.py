import asyncio
from src.kali_mcps.base.kali_command import CommandRunner

class TsharkCommand(CommandRunner):
    def __init__(self):
        super().__init__("tshark", 
                        network_enabled=True,  # 需要网络访问
                        memory_limit="2g",     # 需要更多内存
                        timeout=300)           # 需要更长的超时时间

def capture_live_action(interface: str, duration: int = 30, filter: str = "") -> tuple[str, str]:
    """
    Capture live traffic from network interface
    For example: tshark -i eth0 -a duration:30 -f "port 80"
    """
    cmd = TsharkCommand()
    command = ["tshark", "-i", interface, "-a", f"duration:{duration}"]
    if filter:
        command.extend(["-f", filter])
    return cmd.execute(command)

def analyze_pcap_action(pcap_file: str, display_filter: str = "") -> tuple[str, str]:
    """
    Analyze existing pcap file
    For example: tshark -r file.pcap -Y "http"
    """
    cmd = TsharkCommand()
    command = ["tshark", "-r", pcap_file]
    if display_filter:
        command.extend(["-Y", display_filter])
    return cmd.execute(command)

def extract_http_action(pcap_file: str) -> tuple[str, str]:
    """
    Extract HTTP objects from pcap file
    For example: tshark -r file.pcap -Y "http" -T fields -e http.request.method -e http.request.uri
    """
    cmd = TsharkCommand()
    command = [
        "tshark", "-r", pcap_file,
        "-Y", "http",
        "-T", "fields",
        "-e", "http.request.method",
        "-e", "http.request.uri"
    ]
    return cmd.execute(command)

def protocol_hierarchy_action(pcap_file: str) -> tuple[str, str]:
    """
    Show protocol hierarchy statistics
    For example: tshark -r file.pcap -q -z io,phs
    """
    cmd = TsharkCommand()
    command = ["tshark", "-r", pcap_file, "-q", "-z", "io,phs"]
    return cmd.execute(command)

def conversation_statistics_action(pcap_file: str) -> tuple[str, str]:
    """
    Show conversation statistics
    For example: tshark -r file.pcap -q -z conv,ip
    """
    cmd = TsharkCommand()
    command = ["tshark", "-r", pcap_file, "-q", "-z", "conv,ip"]
    return cmd.execute(command)

def expert_info_action(pcap_file: str) -> tuple[str, str]:
    """
    Show expert information (errors, warnings, notes)
    For example: tshark -r file.pcap -q -z expert
    """
    cmd = TsharkCommand()
    command = ["tshark", "-r", pcap_file, "-q", "-z", "expert"]
    return cmd.execute(command)

if __name__ == "__main__":
    # Test example
    pcap_file = "capture.pcap"
    print(protocol_hierarchy_action(pcap_file))
