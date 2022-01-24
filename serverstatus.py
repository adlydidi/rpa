import ipaddress
import socket
from typing import List
import psutil
from pydantic import BaseModel, json
# from netifaces import interfaces, ifaddresses, AF_INET



class serverStats(BaseModel):
    cpu_usage: str
    mem_percentage: float
    hostname: str
    host_ip: List[ipaddress.IPv4Address] = None



def getStats():
    ss = serverStats(
        cpu_usage=psutil.cpu_percent(interval=0),
        mem_percentage= psutil.virtual_memory()[2],
        hostname= socket.gethostname(),
        host_ip= list(get_ip_addresses(socket.AF_INET))
    )

    # [i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)]
    # print(ss.dict())
    return ss.dict()

def get_ip_addresses(family):
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == family:
                # yield (interface, snic.address)
                yield (snic.address)

# ipv4s = list(get_ip_addresses(socket.AF_INET))
# ipv6s = list(get_ip_addresses(socket.AF_INET6))

# getStats()

# print (ipv4s)