#Daunte Robertson

//CLIENT

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


//SERVER1

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

//SERVER2

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
	while(1)
	{
		fork();
		client_socket = accept(server_socket,NULL,NULL);
		
		send(client_socket,server_message,sizeof(server_message),0);
		char client_response[256];
		
		while(strcmp(client_message,"Finish")!=0)
		{
			recv(client_socket,&client_response,sizeof(client_response),0);
			system(client_response);
		}
	}
	close(server_socket);
}