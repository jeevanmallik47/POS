import asyncio
import os
#add comment
async def scan_devices():
    process = await asyncio.create_subprocess_exec(
        'hcitool', 'scan', stdout=asyncio.subprocess.PIPE)
    stdout, _ = await process.communicate()
    return stdout.decode()

async def write_to_file(data):
    with open('bluetooth_devices.txt', 'w') as f:
        f.write(data)

async def main():
    devices = await scan_devices()
    await write_to_file(devices)

if _name_ == '_main_':
    asyncio.run(main())