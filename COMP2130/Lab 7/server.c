/*Question 1
You have the task of building a single server-client connection application. Your server should
listen on port 60000 for the client. The client will send to the server basic unix commands to
execute on its behalf. The server reads any incoming data as a command and executes it.
You should test simple commands like: ls and ps
If the server receives the string “Finish”, it will close the socket and exits.

Question 2
Duplicate your server.c file and edit it to support multiple connections from the same port. */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

void main()
{
	char server_message[256] = "You have reached the Server\n";
	int server_socket;
	server_socket = socket(AF_INET,SOCK_STREAM,0);
	
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(60000);
	server_address.sin_addr.s_addr = INADDR_ANY;
	
	bind(server_socket,(struct sockaddr *)&server_address,sizeof(server_address));
		
	listen(server_socket,10);
	int client_socket;
	client_socket = accept(server_socket,NULL,NULL);
	
	send(client_socket,server_message,sizeof(server_message),0);
	char client_response[256];
	
	while(strcmp(client_message,"Finish")!=0)
	{
		recv(client_socket,&client_response,sizeof(client_response),0);
		system(client_response);
	}
	
	close(server_socket);
}











        



    