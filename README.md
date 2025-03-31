# awsome-kali-MCPServers

## Overview
Welcome to awsome-kali-MCPServers! This repository is a collection of Model Context Protocol (MCP) servers designed specifically for Kali Linux environments. The goal is to enhance reverse engineering, security testing, and automation workflows by integrating powerful tools and flexible features. Whether you're a security researcher or a developer, this project aims to streamline your tasks with Kali Linux.

## What to Expect
Network Analysis: Tools for sniffing and analyzing traffic.
Binary Understanding: Support for reverse engineering and function analysis.
Automation: Scripts and servers to simplify repetitive tasks.

## New Features
Since the last update, we have added the following features, integrating a series of tools based on the FastMCP framework:

### 1. Network Scanning (Nmap)
- `basic_scan`: Basic network scanning.
- `intense_scan`: In-depth network scanning.
- `stealth_scan`: Stealth network scanning.
- `quick_scan`: Quick network scanning.
- `vulnerability_scan`: Vulnerability scanning.

### 2. Symbol Analysis (nm)
- `basic_symbols`: Lists basic symbols.
- `dynamic_symbols`: Lists dynamic symbols.
- `demangle_symbols`: Decodes symbols.
- `numeric_sort`: Sorts symbols numerically.
- `size_sort`: Sorts symbols by size.
- `undefined_symbols`: Lists undefined symbols.

### 3. Binary Analysis (objdump)
- `file_headers`: Lists file headers.
- `disassemble`: Disassembles the target file.
- `symbol_table`: Lists the symbol table.
- `section_headers`: Lists section headers.
- `full_contents`: Lists full contents.

### 4. String Extraction (strings)
- `basic_strings`: Basic string extraction.
- `min_length_strings`: Extracts strings with a specified minimum length.
- `offset_strings`: Extracts strings with offsets.
- `encoding_strings`: Extracts strings based on encoding.

### 5. Network Traffic Analysis (Wireshark/tshark)
- `capture_live`: Captures network traffic in real-time.
- `analyze_pcap`: Analyzes pcap files.
- `extract_http`: Extracts HTTP data.
- `protocol_hierarchy`: Lists protocol hierarchy.
- `conversation_statistics`: Provides conversation statistics.
- `expert_info`: Analyzes expert information.
### 6. Sandbox Support (Docker)
A new sandbox feature has been added, enabling secure command execution in an isolated container environment:

Runs commands using Docker containers, with the default image being ubuntu-systemd:22.04.
Configurable memory limit (default: 2GB), CPU limit (default: 1 core), network mode, and timeout duration.
Supports bidirectional file copying between the host and the container.
Automatically cleans up container resources.


## TODO
- [ ] **Docker Sandbox Support**: Add containerized environments for safe testing and execution.
- [ ] **Network Tools Integration**: Support for tools like Nmap and Wireshark for advanced network analysis.
- [ ] **Reverse Engineering Tools**: Integrate Ghidra and Radare2 for enhanced binary analysis.
- [ ] **Agent Support**: Enable agent-based functionality for distributed tasks or remote operations.
 
## Current Status
This project is still in its early stages. I’m working on preparing the content, including server configurations, tool integrations, and documentation. Nothing is fully ready yet, but stay tuned—exciting things are coming soon!

## Stay Updated
Feel free to star or watch this repository to get updates as I add more features and files. Contributions and suggestions are welcome once the groundwork is laid out.
