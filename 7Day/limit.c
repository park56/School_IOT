#include <sys/time.h>
#include <sys/resource.h>
#include <stdio.h>

int main() {
	struct rlimit rlim;
	
	// 현제 시스템에서 생성 가능한 프로세스
	getrlimit(RLIMIT_NPROC, &rlim);
	printf("max user proccess : %lu / %lu\n", rlim.rlim_cur, rlim.rlim_max);
	
	// 오픈 가능한 파일의 수
	getrlimit(RLIMIT_NOFILE, &rlim);
	printf("file size : %lu / %lu\n", rlim.rlim_cur, rlim.rlim_max);
	
	// 프로세스가 얻을 수 있는 최대 메모리
	getrlimit(RLIMIT_RSS, &rlim);
	printf("max memory size : %lu / %lu\n", rlim.rlim_cur, rlim.rlim_max);
	
	// 초 단위 CPU시간
	getrlimit(RLIMIT_CPU, &rlim);
	if(rlim.rlim_cur == RLIM_INFINITY) {	// 무한 사용가능한 CPU일 경우
		printf("cpu time : UNLIMIT\n");
	}
	return 0;
}
