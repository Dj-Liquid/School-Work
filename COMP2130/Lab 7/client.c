
	/* Single server-client connection. Small modifications by C. Busby-Earle */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

void main()
{
	int client_socket;
	client_socket = socket(AF_INET,SOCK_STREAM,0);
	
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(60000);
	server_address.sin_addr.s_addr = INADDR_ANY;
	
	int connection_status = connect(client_socket,(struct sockaddr *)&server_address,sizeof(server_address));
	
	if(connection_status == -1)
	{
		printf("There was an error making a connection to the socket");
	}
		
	char server_response[256];
	recv(client_socket,&server_response,sizeof(server_response),0);
	
	printf("The server sent the data: %s",server_response);
	
	while(strcmp(client_message,"Finish")!=0)
	{
		printf("Command for the Server: \n");
		scanf("%s",client_message);
		send(client_socket,client_message,sizeof(client_message),0);
	}
	
	close(client_socket);
}