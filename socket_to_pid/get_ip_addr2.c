#include <stdio.h>      
#include <sys/types.h>
#include <ifaddrs.h>
#include <netinet/in.h> 
#include <string.h> 
#include <arpa/inet.h>

int main (int argc, const char * argv[]) {
    struct ifaddrs * ifAddrStruct=NULL;
    void * tmpAddrPtr=NULL;
    char * addressBuffer=NULL;
    char *local_ip_addr[10];
    int local_ip_addr_index=0;
    int  local_ip_addr_size=0;
    getifaddrs(&ifAddrStruct);

    while (ifAddrStruct!=NULL) {
        if (ifAddrStruct->ifa_addr->sa_family==AF_INET) { // check it is IP4
            // is a valid IP4 Address
            tmpAddrPtr=&((struct sockaddr_in *)ifAddrStruct->ifa_addr)->sin_addr;
            //char addressBuffer[INET_ADDRSTRLEN];
            addressBuffer=(char *) calloc(1,INET_ADDRSTRLEN);
            inet_ntop(AF_INET, tmpAddrPtr, addressBuffer, INET_ADDRSTRLEN);
            local_ip_addr[local_ip_addr_index]=addressBuffer; 
            local_ip_addr_index++;
            local_ip_addr_size++;
            printf("%s IP Address %s\n", ifAddrStruct->ifa_name, addressBuffer); 
            }
        ifAddrStruct=ifAddrStruct->ifa_next;
    }
    for(local_ip_addr_index=0; local_ip_addr_index<local_ip_addr_size;local_ip_addr_index++)
     {
     printf("IP Address %s\n", local_ip_addr[local_ip_addr_index]);          

     }
    return 0;
}
