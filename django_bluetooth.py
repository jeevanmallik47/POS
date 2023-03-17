import asyncio
from django.http import HttpResponse

async def scan_devices():
    proc = await asyncio.create_subprocess_exec(
        'bluetoothctl',
        'scan', 'on',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()

    devices = set()
    for line in stdout.decode().split('\n'):
        if 'Device' in line:
            mac = line.split(' ')[-1]
            devices.add(mac)

    with open('devices.txt', 'w') as f:
        f.write('\n'.join(devices))

def scan_devices_view(request):
    asyncio.run(scan_devices())
    with open('devices.txt', 'r') as f:
        devices = f.read()
    return HttpResponse(devices)
