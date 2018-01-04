#!/usr/bin/python3

import sys
import os

import re

local_addr=sys.argv[1]
peer_addr=sys.argv[2]

cmd="ss -apn"
log=os.popen(cmd,'r',1)


pair_ptn=r'.*?('+local_addr+r').*?('+peer_addr+r').*?pid=(\d+).*?'
pid_ptn=r'.*?pid=(\d+).*?'
#print(normal_syscall_ptn)

pair_ptn_cmpiled=re.compile(pair_ptn)
pid_ptn_cmpiled=re.compile(pid_ptn)

#log=sys.stdin


g_pid_list=""

while True:
    line=log.readline()
    if not line : break
    #print(line.strip())
    #print("================")
    result1=re.findall(pair_ptn_cmpiled,line)
    if result1 :
        #print("+++++++++++++++")
        #print(line.strip())
        print(result1)
        result2=re.findall(pid_ptn_cmpiled,line)
        result3=list(set(result2))
        result3.sort()
        g_pid_list=",".join(result3)
        #print(result3)
        #print("================")
        #print(result1.group(1))
        #print(result1.group(2))
        #print(result1.group(3))


#print g_pid_list
sys.stdout.write(g_pid_list)
print()
