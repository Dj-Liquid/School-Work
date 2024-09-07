//Daunte Robertson


/* Q(1) Write the Linux/Windows command(s) on one line in the shell, that will list all running
processes only on a system and sends these directly to a file by the name
activeProcesses.txt i.e. it will not display its result on the screen, the result will be in the
file which will have to be viewed using an editor or shell command such as less/more.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>

void main ()
{
	system("tasklist > activeProcesses.txt");
}


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


/*or Questions 3 and 4, you will be exploring the use of the exec() family of systems calls
and the wait() system call. You have not done these calls as yet, so you will have to do a
little bit of research.
Q(3.) Write a short program using execvp() that will replace its current execution with the
system command: ls -l (in Windows use CreateProcess and attrib) */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>
#include <unistd.h>

void main()
{
	HANDLE hProcess=NULL;
	HANDLE hThread=NULL;
	STARTUPINFO si;
	PROCESS_INFORMATION pi;
	DWORD dwProcessId=0;
	DWORD dwThreadId=0;
	ZeroMemory(&si,sizeof(si));
	ZeroMemory(&pi,sizeof(pi));
	BOOL bCreateProcess;
	bCreateProcess=CreateProcess("C:\\WINDOWS\\system32\\cmd.exe",NULL,NULL,NULL,FALSE,0,NULL,NULL,&si,&pi);	
	
	system("ls -l");
	WaitForSingleObject(pi.hProcess,INFINITE);
	
	CloseHandle(pi.hThread);
	CloseHandle(pi.hProcess);
	printf("test");
}


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
