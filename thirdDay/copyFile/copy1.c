#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char* orgFile = argv[1];
	char* copyFile = argv[2];
	
	char buff[1024];
	
	int orgRead;
	
	int orgfd;	// 원본 파일 정보
	int copyfd; // 새로 쓰는 파일 정보 
		
	orgfd = open(orgFile, O_RDONLY);
	copyfd = open(copyFile, O_WRONLY|O_CREAT|O_TRUNC, S_IRUSR|S_IWUSR);
	copyfd = open(copyFile, O_WRONLY|O_CREAT|O_TRUNC, 0776);
	
	while(0 < (orgRead = read(orgfd, buff, sizeof(buff)))) {
		write(copyfd, buff, orgRead);
	}
	
	close(orgfd);
	close(copyfd);
	
	return 0;
}
