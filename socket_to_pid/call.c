#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void get_funcname(char* asrc_addr,char* adst_addr)
{
    FILE *fstream=NULL;  
    char buff[400]="";      
    char result[1000]="";
    char cmd[300]="";
   
 
    //memset(result,0,sizeof(result)); 
    sprintf(cmd,"./get_sock_pid2.py %s  %s",asrc_addr,adst_addr);    


    if(NULL==(fstream=popen(cmd,"r")))       
    {      
        fprintf(stderr,"execute command failed: ");       
        return;       
    }      
    while(NULL!=fgets(buff, sizeof(buff), fstream))      
    {   
        strcat(result,buff);       
    }
    printf("%s",result);
    pclose(fstream);   
}


int main(int argc, char *argv[])
{

 
    char src_addr[100]="192.168.159.137:22";
    char dst_addr[100]="192.168.159.1:50727";
    get_funcname(src_addr,dst_addr);

}
