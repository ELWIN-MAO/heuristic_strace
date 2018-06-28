#!/usr/bin/python3

import sys
import os

import re

import shutil


trace_type=sys.argv[1]
unix_tcp_port=sys.argv[2]


file_name = os.listdir('.')
for temp in file_name:
    if not( temp=="h-strace.py" or temp=="gengraph2.sh"):
        os.remove(temp)


os.system("ls")

if not os.path.exists("gengraph2.sh"):
    shutil.copy("../gengraph2.sh", "./gengraph2.sh") 

os.system("ls")

#sys.exit()

pid_list=[]

def unix_soket_process():
    print("222")
    cmd="sudo ss -lpn"
    log=os.popen(cmd,'r',1)
    pid_ptn=r'.*?pid=(\d+).*?'
    pid_ptn_cmpiled=re.compile(pid_ptn)
    unix_pairt_ptn=r'u_str(\ )+LISTEN(\ )+[\d]+(\ )+[\d]+(\ )+((\S*) (\d+))(\ )+((\S*) (\d+))(\ )+.*?pid=(\d+).*'
    unix_pairt_ptn_cmpiled=re.compile(unix_pairt_ptn)

    while True:
        line=log.readline()
        if not line : break
        result1=unix_pairt_ptn_cmpiled.match(line)
        #if result1:
        #    print("result1,5")
        #    print(result1.group(5))
        #    print("result1,7")
        #    print(result1.group(7))
        #    print(result1.group(5)==local_addr) 
        #    print(result1.group(7)==peer_addr)
        if result1 and (result1.group(6)==unix_tcp_port) :
        #if result1:
            print("result1:"+line)
            #print(line)
            #print(peer_inode)
            result2=re.findall(pid_ptn_cmpiled,line)
            print("result2:")
            print(result2)
            if "1" in result2:
                result2.remove("1")
            result3=list(set(result2))
            result3.sort()
            for aitem in result3:
                pid_list.append(aitem)


def tcp_soket_process():
    print("1111")
    cmd="sudo ss -lpn"
    log=os.popen(cmd,'r',1)
    pid_ptn=r'.*?pid=(\d+).*?'
    pid_ptn_cmpiled=re.compile(pid_ptn)
    tcp_pair_ptn=r'tcp(\ )+LISTEN(\ )+[\d]+(\ )+[\d]+(\ )+(.*:(\d+))(\ )+((.*:.*)+)(\ )+.*?pid=(\d+).*'
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
        if result1 and (result1.group(6)==unix_tcp_port) :
        #if result1:
            print("result1:"+line)
            #print(line)
            #print(peer_inode)
            result2=re.findall(pid_ptn_cmpiled,line)
            print("result2:")
            print(result2)
            if "1" in result2:
                result2.remove("1")
            result3=list(set(result2))
            result3.sort()
            for aitem in result3:
                pid_list.append(aitem)
            


def xwindow_process():
    cmd="xprop _NET_WM_PID"
    log=os.popen(cmd,'r',1)
    pid_ptn=r'_NET_WM_PID\(CARDINAL\) = (\d+)'
    pid_ptn_cmpiled=re.compile(pid_ptn)
    while True:
        line=log.readline()
        if not line : break
        result1=pid_ptn_cmpiled.match(line)
        if result1: 
            pid=result1.group(1)
            print(pid)
        # string to int
            pid_list.append(pid)
        # pid_list.jion","

if trace_type=="TCP":
    tcp_soket_process()
elif trace_type=="UNIX":
    unix_soket_process()
elif trace_type=="XWINDOW":
    xwindow_process()
else:
    print("error")


print(pid_list)
pid_list=list(set(pid_list))
print(pid_list)
cmd="sudo ../strace  -ff -o tst.log -y -yy  -s 200 -v -p "+(",".join(pid_list))
print(cmd)
fo = open("./aaa", "w")
log=os.popen(cmd,'r',1)
while True:
    line=log.readline()
    if not line : break
    fo.write(line)
