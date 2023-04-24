#include <stdio.h>
#include <time.h>
#include <sys/time.h>

int main(int argc, char* argv[]) {
	
	time_t rawtime;
	time(&rawtime);   // 현재 시간 받기
	printf("time: %u\n", (unsigned)rawtime);	
	
	struct timeval my_timeval;
	gettimeofday(&my_timeval, NULL);
	printf("gettimeofday: %u/%u\n",my_timeval.tv_sec, my_timeval.tv_usec);	
	
	printf("ctime: %s", ctime(&rawtime));
	
	struct tm * timeinfo;
	char buffer [80];
	timeinfo = localtime (&rawtime);
	
	printf("localtime: %s", asctime(timeinfo));
	
	strftime (buffer,80,"%c",timeinfo);
	printf("strftime: %s\n", buffer);
 
	return 0;
}
