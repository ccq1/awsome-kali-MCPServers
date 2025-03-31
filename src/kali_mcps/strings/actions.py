import asyncio
from src.kali_mcps.base.kali_command import KaliCommand

class StringsCommand(KaliCommand):
    def __init__(self):
        super().__init__("strings", network_enabled=False, memory_limit="1g", timeout=120)

async def basic_strings(target: str, input_file: bytes = None) -> tuple[str, str]:
    """
    Basic strings analysis
    For example: strings /path/to/file
    """
    cmd = StringsCommand()
    command = ["strings", target]
    return await cmd.execute(command, input_files={"input_file": "/tmp/input_file"})

async def min_length_strings(target: str, length: int = 6) -> tuple[str, str]:
    """
    Strings analysis with specified minimum length
    For example: strings -n 6 /path/to/file
    """
    cmd = StringsCommand()
    command = ["strings", "-n", str(length), target]
    return await cmd.execute(command)

async def offset_strings(target: str, format: str = "x") -> tuple[str, str]:
    """
    Strings analysis showing string offsets
    format can be: 'd' (decimal), 'o' (octal), 'x' (hexadecimal)
    For example: strings -t x /path/to/file
    """
    cmd = StringsCommand()
    command = ["strings", "-t", format, target]
    return await cmd.execute(command)

async def encoding_strings(target: str, encoding: str = "S") -> tuple[str, str]:
    """
    Strings analysis with specified character encoding
    encoding can be: 
    - 's' = 7-bit string
    - 'S' = 8-bit string
    - 'b' = 16-bit big-endian
    - 'l' = 16-bit little-endian
    For example: strings -e S /path/to/file
    """
    cmd = StringsCommand()
    command = ["strings", "-e", encoding, target]
    return await cmd.execute(command)

if __name__ == "__main__":
    # Test example
    target_file = "/bin/ls"
    input_file = bytes.fromhex("68656c6c6f20776f726c64")
    print(asyncio.run(basic_strings(target_file, {"input_file": input_file , "output_file": "/tmp/output_file"})))
