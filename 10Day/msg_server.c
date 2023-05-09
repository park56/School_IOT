#include <stdio.h>
#include <unistd.h>
#include <sys/msg.h>

#define MSQKEY 51234

struct msgbuf {
	long mtype;
	char mtext[BUFSIZ];
};

int main(int argc, char* argv[]) {
	key_t key;
	int n, msqid;
	struct msgbuf mb;
	
	key = MSQKEY;
	
	// 메시지 큐의 채널을 생성
	if((msqid = msgget(key, IPC_CREAT | IPC_EXCL | 0666)) < 0) {
		perror("msgget()");
		return -1;
	}
	
	// 메시지큐애서 데이터 가져옴
	while((n= msgrcv(msqid, &mb, sizeof(mb), 0, 0)) > 0) {
		switch (mb.mtype) {
			// 메시지 타입이 1이면 화면에 가져온 데이터를 출력
			case 1:
				write(1, mb.mtext, n);
				break;
			// 메시지 타입이 2이면 메시지큐의 채널을 삭제
			case 2:
				if(msgctl(msqid, IPC_RMID, (struct msqid_ds *) 0) < 0) {
					perror("msgctl()");
					return -1;
				}
				break;
		}
	}
	return 0;
}
