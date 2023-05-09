#include <stdio.h>
#include <unistd.h>
#include <sys/msg.h>
#include <string.h>
#include <stdlib.h>

#define MSQKEY 51234	

struct msgbuf {
	long mtype;
	char mtext[BUFSIZ];
};

int main(int argc, char **argv) {
	key_t key;
	int rc, msqid;
	char *msg_text = "hello world\n";
	struct msgbuf *mb;
	
	mb = (struct msgbuf*)malloc(sizeof(struct msgbuf) + strlen(msg_text));
	
	key = MSQKEY;
	// 메시지큐의 채널을 가져온다
	if((msqid = msgget(key, 0666)) < 0) {
		perror("msgget()");
		return -1;
	}
	
	// mtype을 2로 설정하고 보낸다
	mb->mtype = 2;
	memset(mb->mtext, 0, sizeof(mb->mtext));
	if(msgsnd(msqid, mb, sizeof(mb->mtext), 0) < 0) {
		perror("msgsnd()");
		return -1;
	}
	return 0;
}
