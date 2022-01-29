import ipaddress
# from nis import cat
from select import select
import sqlite3
import struct
from warnings import catch_warnings
import socket

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))

## create the database and the table
def initDB():
    try:
        conn = sqlite3.connect('rpa.db')
        conn.execute('''CREATE TABLE CLIENTS
        (   HostName            TEXT    NOT NULL,
            HostIp              INT     NOT NULL,
            HostStatus              TEXT    NOT NULL    
        );''')
        conn.close()
        return {"createDB" : "Successfuly initialised"}
    except sqlite3.Error as e:
        return {"createDB" : e}

### registre the client in the Database
def registerClient(hostname, host_ip, clientStatus = 'SLEEP'):
    # try:
    conn = sqlite3.connect('rpa.db')
    host_ip2int = ip2int(host_ip)
    rows = conn.execute("select * from CLIENTS").fetchall()
    ## check to see duplicate clients exists in the database and delete the duplicates
    for row in rows:
        if row[1] == host_ip2int:
            conn.execute("delete from CLIENTS where HostIp = ?", (host_ip2int,) )
    conn.execute("INSERT INTO CLIENTS (HostName, HostIp, HostStatus) VALUES (?,?,?)", (hostname, host_ip2int, clientStatus))
    conn.commit()
    conn.close()
    # except conn.Error as e:
        # initDB()
    return None

### registre the client in the Database
def unregisterClient(hostname, host_ip, clientStatus = 'SLEEP'):
    # try:
    conn = sqlite3.connect('rpa.db')
    host_ip2int = ip2int(host_ip)
    rows = conn.execute("select * from CLIENTS").fetchall()
    ## check to see duplicate clients exists in the database and delete the duplicates
    for row in rows:
        if row[1] == host_ip2int:
            conn.execute("delete from CLIENTS where HostIp = ?", (host_ip2int,) )
    # conn.execute("INSERT INTO CLIENTS (HostName, HostIp, HostStatus) VALUES (?,?,?)", (hostname, host_ip2int, clientStatus))
    conn.commit()
    conn.close()
    # except conn.Error as e:
        # initDB()
    return {"ClientName" : hostname, "ClientIP" : host_ip, "message" : "unregistered"}



def selectAllClients():
    conn = sqlite3.connect('rpa.db')
    rows = conn.execute("select * from CLIENTS").fetchall()
    # for row in rows:
    #     print(row)
    conn.close()
    return rows


# dbInit = initDB()
# # print(dbInit)
# # # # myip = ipaddress.IPv4Address('192.168.1.1')
# # myip = '192.168.1.1'
# # myipint = ip2int(myip)
# # # print(myipint)
# # myintip = int2ip(myipint)
# # # print(myintip)

# # registerClient('TESTPC', myip )
# registerClient('TESTPC', '192.168.1.1')


# r = selectAllClients()
# r = unregisterClient('TESTPC', '192.168.1.1')
# print(r)