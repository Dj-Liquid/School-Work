/*Q(2) Write a program where the parent process will create a file for writing by the name
myfile.txt. The parent should spawn a child process that will then write the text:
'I am a child'
'I am writing in this file'
'My process id is 9999'
The dummy value 9999 should be replaced by the process ID of the process writing to the
file.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>
#include <unistd.h>

DWORD WINAPI ThreadFun(LPVOID lpParam)
{
	//printf("Thread Running");
	return 0;
}

void main()
{
	FILE *fpt;
	int parent;
	HANDLE hThread;
	DWORD ThreadID;
	fpt=fopen("myfile.txt","w");
	parent=getpid();
	hThread = CreateThread(NULL,0,ThreadFun,NULL,0,&ThreadID);
	if(ThreadID!=parent)
	{
		fprintf(fpt,"I am a child\nI am writing in this file\nMy process id is %d",ThreadID);
	}
	CloseHandle(hThread);
	fclose(fpt);
}