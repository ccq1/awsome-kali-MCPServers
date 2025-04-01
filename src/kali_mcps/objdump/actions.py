import asyncio
from src.kali_mcps.base.kali_command import CommandRunner

class ObjdumpCommand(CommandRunner):
    def __init__(self):
        super().__init__("objdump", network_enabled=False, memory_limit="1g", timeout=120)

async def file_headers_action(target: str) -> tuple[str, str]:
    """
    Display file headers
    For example: objdump -f /path/to/file
    """
    cmd = ObjdumpCommand()
    command = ["objdump", "-f", target]
    return await cmd.execute(command)

async def disassemble_action(target: str, section: str = ".text") -> tuple[str, str]:
    """
    Disassemble section (default: .text)
    For example: objdump -d -j .text /path/to/file
    """
    cmd = ObjdumpCommand()
    command = ["objdump", "-d", "-j", section, target]
    return await cmd.execute(command)

async def symbol_table_action(target: str) -> tuple[str, str]:
    """
    Display symbol table
    For example: objdump -t /path/to/file
    """
    cmd = ObjdumpCommand()
    command = ["objdump", "-t", target]
    return await cmd.execute(command)

async def section_headers_action(target: str) -> tuple[str, str]:
    """
    Display all section headers
    For example: objdump -h /path/to/file
    """
    cmd = ObjdumpCommand()
    command = ["objdump", "-h", target]
    return await cmd.execute(command)

async def full_contents_action(target: str) -> tuple[str, str]:
    """
    Display all information including headers and disassembly
    For example: objdump -x /path/to/file
    """
    cmd = ObjdumpCommand()
    command = ["objdump", "-x", target]
    return await cmd.execute(command)

if __name__ == "__main__":
    # Test example
    target_file = "/bin/ls"
    print(asyncio.run(file_headers_action(target_file)))
