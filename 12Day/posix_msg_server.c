#include <stdio.h>
#include <unistd.h>
#include <mqueue.h>

int main(int argc, char *argv[]){
	mqd_t mq;
	struct mq_attr attr;
	const char* name = "/posix_msq";
	char buf[BUFSIZ];
	int n;
	
	// 메시지 큐 속성 초기화
	attr.mq_flags = 0;
	attr.mq_maxmsg = 10;
	attr. mq_msgsize = BUFSIZ;
	attr.mq_curmsgs = 0;
	
	mq = mq_open(name, O_CREAT | O_RDONLY, 0644, &attr);
	
	// 메시지 큐에서 데이터  가져옴
	while(1) {
		n = mq_receive(mq, buf, sizeof(buf), NULL);
		switch(buf[0]){
			// 메시지가 q이면 END로 이동
			case 'q':
				goto END;
				break;
			// 다른 메시지면 화면에 가져온 데이터 출력
			default:
				write(1, buf, n);
				break;
		}
	}
	
	
// 메시지 큐를 닫은 후 정리하고 프로그램 종료
END:
	mq_close(mq);
	mq_unlink(name);
	
	return 0;
}
