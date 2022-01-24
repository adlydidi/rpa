import ipaddress
from nis import cat
from select import select
import sqlite3
import struct
from warnings import catch_warnings
import socket

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))

def initDB():
    try:
        conn = sqlite3.connect('rpa.db')
        conn.execute('''CREATE TABLE CLIENTS
        (HostName           TEXT    NOT NULL,
        HostIp            INT     NOT NULL);''')
        conn.close()
        return {"createDB" : "Successfuly initialised"}
    except sqlite3.Error as e:
        return {"createDB" : e}
def registerClient(hostname, host_ip):
    conn = sqlite3.connect('rpa.db')
    host_ip2int = ip2int(host_ip)
    rows = conn.execute("select * from CLIENTS").fetchall()
    for row in rows:
        if row[1] == host_ip2int:
            conn.execute("delete from clients where HostIp = ?", (host_ip2int,) )
    conn.execute("INSERT INTO CLIENTS (HostName, HostIp) VALUES (?,?)", (hostname, host_ip2int));
    conn.commit()
    conn.close()
    return None

def selectAllClients():
    conn = sqlite3.connect('rpa.db')
    rows = conn.execute("select * from CLIENTS").fetchall()
    for row in rows:
        print(row)
    return None


# dbInit = initDB()
# print(dbInit)
# # myip = ipaddress.IPv4Address('192.168.1.1')
myip = '192.168.1.1'
myipint = ip2int(myip)
print(myipint)
myintip = int2ip(myipint)
print(myintip)

registerClient('TESTPC', myip )


selectAllClients()
