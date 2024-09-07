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
