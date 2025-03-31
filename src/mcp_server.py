from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
import os
from src.kali_mcps.nmap.actions import basic_scan, intense_scan, stealth_scan, quick_scan, vulnerability_scan
from src.kali_mcps.nm.actions import basic_symbols, dynamic_symbols, demangle_symbols, numeric_sort, size_sort, undefined_symbols
from src.kali_mcps.objdump.actions import file_headers, disassemble, symbol_table, section_headers, full_contents
from src.kali_mcps.strings.actions import basic_strings, min_length_strings, offset_strings, encoding_strings
from src.kali_mcps.wireshark.actions import capture_live, analyze_pcap, extract_http, protocol_hierarchy, conversation_statistics, expert_info

mcp = FastMCP("kali-tools")


IS_SAFE = os.environ.get("IS_SAFE", "false").lower() == "true"  # is safe mode, if true, the command will be executed in the sandbox

# nmap start
@mcp.tool()
def basic_scan(target: str):
    """Perform a basic network scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the basic scan.
    """
    return basic_scan(target)

@mcp.tool()
def intense_scan(target: str):
    """Perform an intense network scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the intense scan.
    """
    return intense_scan(target)

@mcp.tool()
def stealth_scan(target: str):
    """Perform a stealth network scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the stealth scan.
    """
    return stealth_scan(target)

@mcp.tool()
def quick_scan(target: str):
    """Perform a quick network scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the quick scan.
    """
    return quick_scan(target)

@mcp.tool()
def vulnerability_scan(target: str):
    """Perform a vulnerability scan using nmap.

    Args:
        target (str): The target IP address or hostname to scan.

    Returns:
        str: The output results of the vulnerability scan.
    """
    return vulnerability_scan(target)
# nmap end

# nm start
@mcp.tool()
def basic_symbols(target: str):
    """Perform a basic symbol listing using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the basic symbol listing.
    """
    return basic_symbols(target)

@mcp.tool()
def dynamic_symbols(target: str):
    """Perform a dynamic symbol listing using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the dynamic symbol listing.
    """
    return dynamic_symbols(target)

@mcp.tool()
def demangle_symbols(target: str):
    """Perform a demangling of symbols using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the demangling of symbols.
    """
    return demangle_symbols(target)

@mcp.tool()
def numeric_sort(target: str):
    """Perform a numeric sort of symbols using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the numeric sort of symbols.
    """
    return numeric_sort(target)

@mcp.tool()
def size_sort(target: str):
    """Perform a size sort of symbols using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the size sort of symbols.
    """
    return size_sort(target)

@mcp.tool()
def undefined_symbols(target: str):
    """Perform an undefined symbol listing using nm.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the undefined symbol listing.
    """
    return undefined_symbols(target)
# nm end

# objdump start
@mcp.tool()
def file_headers(target: str):
    """Perform a file header listing using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the file header listing.
    """
    return file_headers(target)

@mcp.tool()
def disassemble(target: str):
    """Perform a disassembly of the target file using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the disassembly of the target file.
    """
    return disassemble(target)

@mcp.tool()
def symbol_table(target: str):
    """Perform a symbol table listing using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the symbol table listing.
    """
    return symbol_table(target)

@mcp.tool()
def section_headers(target: str):
    """Perform a section header listing using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the section header listing.
    """
    return section_headers(target)

@mcp.tool()
def full_contents(target: str):
    """Perform a full contents listing using objdump.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the full contents listing.
    """
    return full_contents(target)
# objdump end

# strings start
@mcp.tool()
def basic_strings(target: str):
    """Perform a basic string listing using strings.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the basic string listing.
    """
    return basic_strings(target)

@mcp.tool()
def min_length_strings(target: str):
    """Perform a minimum length string listing using strings.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the minimum length string listing.
    """
    return min_length_strings(target)

@mcp.tool()
def offset_strings(target: str):
    """Perform an offset string listing using strings.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the offset string listing.
    """
    return offset_strings(target)

@mcp.tool()
def encoding_strings(target: str):
    """Perform an encoding string listing using strings.

    Args:
        target (str): The target file or executable to analyze.

    Returns:
        str: The output results of the encoding string listing.
    """
    return encoding_strings(target)
# strings end

# tshark start
@mcp.tool()
def capture_live(interface: str, duration: int = 30, filter: str = ""):
    """Perform a live capture of network traffic using tshark.

    Args:
        interface (str): The network interface to capture from.
        duration (int): The duration of the capture in seconds.
        filter (str): The filter to apply to the capture.

    Returns:
        str: The output results of the live capture of network traffic.
    """
    return capture_live(interface, duration, filter)


@mcp.tool()
def analyze_pcap(pcap_file: str, display_filter: str = ""):
    """Perform an analysis of a pcap file using tshark.

    Args:
        pcap_file (str): The path to the pcap file to analyze.
        display_filter (str): The filter to apply to the analysis.

    Returns:
        str: The output results of the analysis of the pcap file.
    """
    return analyze_pcap(pcap_file, display_filter)

@mcp.tool()
def extract_http(pcap_file: str):
    """Perform an HTTP extraction from a pcap file using tshark.

    Args:
        pcap_file (str): The path to the pcap file to extract HTTP from.    

    Returns:
        str: The output results of the HTTP extraction from the pcap file.
    """
    return extract_http(pcap_file)  

@mcp.tool()
def protocol_hierarchy(pcap_file: str):
    """Perform a protocol hierarchy listing using tshark.

    Args:
        pcap_file (str): The path to the pcap file to analyze.  

    Returns:
        str: The output results of the protocol hierarchy listing.
    """
    return protocol_hierarchy(pcap_file)    

@mcp.tool()
def conversation_statistics(pcap_file: str):
    """Perform a conversation statistics listing using tshark.

    Args:
        pcap_file (str): The path to the pcap file to analyze.  

    Returns:
        str: The output results of the conversation statistics listing.
    """
    return conversation_statistics(pcap_file)   

@mcp.tool() 
def expert_info(pcap_file: str):
    """Perform an expert information listing using tshark.

    Args:
        pcap_file (str): The path to the pcap file to analyze.  

    Returns:
        str: The output results of the expert information listing.
    """
    return expert_info(pcap_file)   
# tshark end

# run server, using stdio transport
if __name__ == "__main__":
    print("Starting server is running")
    mcp.run(transport="stdio")