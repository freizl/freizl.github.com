#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
     printf("start main ....\n");
     pid_t pid;
     /* fork another process */
     pid = fork();
     printf("do a fork and get id %d \n",pid);
     if (pid < 0) { /* error occurred */
              fprintf(stderr, "Fork Failed");
              exit(-1);
     }
     else if (pid == 0) { /* child process */
              printf("Enter Child process.....\n");
              execlp("/bin/ls", "ls ~/Desktop", NULL);
              printf("Leave Child process.....\n");
     }
     else { /* parent process */
              printf("Enter parent process.....\n");
              /* parent will wait for the child to complete */
              wait (NULL);
              printf ("Child Complete\n");
              printf("Leave parent process.....\n");
              exit(0);
     }
     printf("end main ....\n");
}

