#include <stdio.h>

#define BUFF_SIZE 1024

int main(int argc, char* argv[])
{
	FILE *orgFile = fopen(argv[1], "r");
	FILE *copyFile = fopen(argv[2], "w");
	
	char buff[BUFF_SIZE];
	
	int fd;
	
	while(0 < (fd = fread(buff, sizeof(long), BUFF_SIZE, orgFile))){
		fwrite(buff, sizeof(long), fd, copyFile);
	}
	
	fclose(orgFile);
	fclose(copyFile);
}
