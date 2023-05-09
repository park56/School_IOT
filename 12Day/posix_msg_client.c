#include <stdio.h>
#include <unistd.h>
#include <mqueue.h>
#include <string.h>

int main(int argc, char* argv[]) {
	mqd_t mq;
	const char* name = "/posix_msq";
	char buf[BUFSIZ];
	
	mq = mq_open(name, O_WRONLY);
	
	// Hello world라는 문자를 보냄
	strcpy(buf, "Hello, World!\n");
	mq_send(mq, buf, strlen(buf), 0);
	
	// q로 설정하고 보냄
	strcpy(buf, "q");
	mq_send(mq, buf, strlen(buf), 0);
	
	// 메시지 큐 닫음
	mq_close(mq);
	
	return 0;
}
