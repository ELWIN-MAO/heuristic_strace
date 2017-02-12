#!/usr/bin/python

import sys

log=sys.stdin
#log=open(sys.argv[1],'r')


mylocal=sys.argv[1]
mypeer=sys.argv[2]

g_pid_list=[]

while True:
    line=log.readline()
    if not line : break
    if line.startswith("ESTAB") :
        words=line.split()
        local=words[3]
        peer=words[4]
        if(cmp(mylocal,local) == 0 and  cmp(mypeer,peer)==0) :
            pid_list=words[5].split(",")
            for aitem in pid_list:
                if aitem.startswith("pid="):
                    g_pid_list.append(aitem[4:])
print g_pid_list
sys.stdout.write(g_pid_list[0])
del(g_pid_list[0])
for aitem in g_pid_list:
    sys.stdout.write(","+aitem)
print
