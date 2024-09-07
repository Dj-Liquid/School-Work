/*Q(4.) Write a program where a parent process will wait on its child process to say the word
“Hello” 50 times. The parent process will ask the child to say the word “Hello” 50 times.
After the child process is finished following the instruction given by the parent, the parent
process will just print : “Well done my child”. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>
#include <unistd.h>
#include <process.h>

DWORD WINAPI ThreadFun(LPVOID lpParam)
{
	//printf("Thread Running");
	return 0;
}

void main()
{
	int parent;
	HANDLE hThread;
	DWORD ThreadID;
	parent=getpid();
	hThread = CreateThread(NULL,0,ThreadFun,NULL,0,&ThreadID);
	if(ThreadID!=parent)
	{
		for(int i=0;i<50;i++)
		{
			printf("Hello\n");
		}
	}
	
	CloseHandle(hThread);
	
	cwait(NULL,ThreadID, _WAIT_CHILD); 
	printf("Well done my child");
}