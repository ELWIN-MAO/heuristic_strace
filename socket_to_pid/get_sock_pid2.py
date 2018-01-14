#!/usr/bin/python3

import sys
import os

import re

socket_type=sys.argv[1]
local_addr=sys.argv[2]
peer_addr=sys.argv[3]

#print(socket_type)
#print(local_addr)
#print(peer_addr)


cmd="ss -apne"
log=os.popen(cmd,'r',1)



#print(normal_syscall_ptn)


pid_ptn=r'.*?pid=(\d+).*?'
pid_ptn_cmpiled=re.compile(pid_ptn)
#log=sys.stdin



def tcp_soket_process():
    g_pid_list=""
    peer_inode=""
    tcp_pair_ptn=r'tcp(\ )+.+(\ )+[\d]+(\ )+[\d]+(\ )+([\d\.\:]+)(\ )+([\d\.\:]+)(\ )+.*?pid=(\d+).*ino\:([\d]+).*'
    tcp_pair_ptn_cmpiled=re.compile(tcp_pair_ptn)

    while True:
        line=log.readline()
        if not line : break
        result1=tcp_pair_ptn_cmpiled.match(line)
        #if result1:
        #    print("result1,5")
        #    print(result1.group(5))
        #    print("result1,7")
        #    print(result1.group(7))
        #    print(result1.group(5)==local_addr) 
        #    print(result1.group(7)==peer_addr)
        if result1 and (result1.group(5)==local_addr) and (result1.group(7)==peer_addr) :
            #print(line)
            peer_inode=result1.group(10)
            #print(peer_inode)
            result2=re.findall(pid_ptn_cmpiled,line)
            #print(result2)
            if "1" in result2:
                result2.remove("1")
            result3=list(set(result2))
            result3.sort()
            g_pid_list=",".join(result3)
    #print g_pid_list
    sys.stdout.write(g_pid_list)
    print()
    sys.stdout.write(peer_inode)
    print()


def unix_soket_process():
    g_pid_list=""
    peer_inode=""
    unix_pair_ptn=r'u_str(\ )+.+(\ )+[\d]+(\ )+[\d]+(\ )+.+(\ )+([\d]+)(\ )+.+(\ )+([\d]+)(\ )+.*?pid=(\d+).*'
    unix_pair_ptn_cmpiled=re.compile(unix_pair_ptn)
    pid_ptn_cmpiled=re.compile(pid_ptn)
    while True:
        line=log.readline()
        if not line : break
        result1=unix_pair_ptn_cmpiled.match(line)
        if result1 and (result1.group(6)==local_addr) and (result1.group(9)==peer_addr) :
            peer_inode=peer_addr
            #print(line.strip())
            result2=re.findall(pid_ptn_cmpiled,line)
            if "1" in result2:
                result2.remove("1")
            result3=list(set(result2))
            result3.sort()
            g_pid_list=",".join(result3)
    #print g_pid_list
    sys.stdout.write(g_pid_list)
    print()
    sys.stdout.write(peer_inode)
    print()



if socket_type=="TCP":
    tcp_soket_process()
else:
    unix_soket_process()

