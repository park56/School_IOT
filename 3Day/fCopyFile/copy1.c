#include <stdio.h>

#define BUFF_SIZE 1024

int main(int argc, char* argv[])
{
	FILE *orgFile = fopen(argv[1], "r");
	
	FILE *copyFile = fopen(argv[2], "w");
	
	char buff[BUFF_SIZE];
	
	int fd;
	int start = 0;
	int end = BUFF_SIZE;
	
	while(0 < (fd = fread(buff, sizeof(char), BUFF_SIZE, orgFile))){
		fwrite(buff, sizeof(char), fd, copyFile);
	}
	
	fclose(orgFile);
	fclose(copyFile);
}
