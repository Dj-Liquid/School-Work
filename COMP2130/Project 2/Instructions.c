Write a program that spawns and controls multiple processes. The program should use system calls to
create, manage and terminate the processes. The program should use signal system calls to
communicate between the processes. The processes should coordinate a simple command structure
where the main process is the “base” and its child processes are “planes”.

The base process is the main process. It should run in a simple loop, prompting the user for an input
command. Valid input commands are,
• launch
• bomb
• refuel
• quit

The bomb and refuel commands each require one(1) argument, the others do not require any. You may
use any variation on the commands, for example “L” for launch instead of the full word. Invalid
commands should produce a suitable error message, including those described below. Upon receiving
the command to quit, the program should terminate.

The launch command should create a child process i.e. a plane to take off. Once launched all child
processes should execute the following (same) code”

• A child process i.e. a “plane” should execute a loop, counting its available quantity of “fuel”
downward, beginning at 100. It loses fuel at a rate of 5 units/second

• Every 3 seconds a plane must report to the base its fuel status by printing the line “Bomber N to
base, #% of fuel left,” where N is the child’s process ID (which as we know, is an integer)

• When the bomb command is entered the base first checks whether or not any planes were
launched. If there were, it prompts for the plane’s (process) ID and sends the plane with process
ID N, the SIGUSR1 signal. Upon receiving this signal the plane with ID N should print the line
“Bomber N to base, bombs away!”. If no planes were launched the message “No planes are
flying, can’t drop a bomb!” must be printed

• When the refuel command is entered the base first checks whether or not any planes were
launched. If there were, it prompts for the plane’s ID and sends the plane with process ID N, the
SIGUSR2 signal. The child process should “refuel” by resetting its fuel value to 100 and
printing the message “Plane N has been refueled”, where N is the plane’s (process) ID

• When a plane’s fuel reaches zero (or less), it should print the message “SoS! Plane N is going to
crash”, again where N is the plane’s (process) ID, and then it exits

The base (parent process) should therefore be able to “know” that at least 1 plane (child process) has
been created.

To properly demonstrate that your code works, it must be able to manage a minimum of 2 planes (child
processes). Remember that the use of the user-defined signals i.e. SIGUSR1 and SIGUSR2, means that
you must write signal handlers for them in your code. Below are samples of the output that depict how
the program should work and that it manages (more than) the minimum required number of processes.

void main()
{
	char command[10];
	int fuel=100,pID;
	
	
	printf("The list of valid commands are\nlaunch\nbomb\nrefuel\nquit\n");
	while(true)
	{
		printf("Enter a command: ");
		scanf("%s",command);
		
		if(strcmp(command,"launch")==0)
		{
			PLACEHOLDER
		}
		else if(strcmp(command,"bomb")==0)
		{
			printf("Enter smn else");
			scanf("",);
			PLACEHOLDER
		}
		else if(strcmp(command,"refuel")==0)
		{
			printf("Enter smn else");
			scanf("",);
			PLACEHOLDER
		}
		else if(strcmp(command,"quit")==0)
		{
			exit(0);
		}
		else
		{
			printf("%s is not a valid command",command);
		}
	}
}



after the first fork() where the plane is put into a loop stating its fuel %, use another fork and a while(1) loop 
to check for when a command is issued towards that specific child.



fix the planes counter (have the child interact with the parent's "planes" variable)

find out how to copy/paste from the virtual machine
