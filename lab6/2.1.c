#include <stdio.h>
#include <unistd.h>

int main(void)
{
  int pid = fork();
  if (pid == 0) {
      printf("Это сообщение из дочернего процесса\nДочерний PID = %d\nРодительский PID = %d\n", pid, getppid());
  }
  return 0;
}
