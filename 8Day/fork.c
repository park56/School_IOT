#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void firstFork();
void newFork();

int main(){
	//firstFork();
	newFork();
}

void firstFork(){
	pid_t pid;
	int x = 1;
	
	pid = fork();
	if(pid == 0) {
		printf("child : x=%d\n", ++x);
		exit(0);
	}
	
	printf("parents: x=%d\n", --x);
	exit(0);
}

void newFork() {
	printf("L0\n");
	if(fork() != 0) {
		printf("L1\n");
		if(fork() != 0) {
			printf("L2\n");
		}
	}
	printf("Bye\n");
}
