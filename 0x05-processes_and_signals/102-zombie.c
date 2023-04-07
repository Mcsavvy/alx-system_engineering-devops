#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <signal.h>

/**
 * infinite_while - runs an infinite while loop
 *
 * Return: nothing
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - creates 5 zombie processes
 *
 * Return: an integer
 */
int main(void)
{
	pid_t pid;
	signal(SIGCHLD, SIG_IGN);

	pid = fork();
	/* child 1 */
	if (pid != 0)
	{
		printf("Zombie process created, PID: %i\n", pid);
		pid = fork();
		/* child 2 */
		if (pid != 0)
		{
			printf("Zombie process created, PID: %i\n", pid);
			pid = fork();
			/* child 3 */
			if (pid != 0)
			{
				printf("Zombie process created, PID: %i\n", pid);
				pid = fork();
				/* child 4 */
				if (pid != 0)
				{
					printf("Zombie process created, PID: %i\n", pid);
					pid = fork();
					/* child 5 */
					if (pid != 0)
					{
						printf("Zombie process created, PID: %i\n", pid);

					}
				}
			}
		}
	}
	infinite_while();
	return (0);
}
