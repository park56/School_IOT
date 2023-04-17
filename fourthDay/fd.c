#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>

int main(int argc, char* argv[]) {
	char* dirName = argv[1];
	char dirPath[32];
	
	int fd = open(dirName, O_WRONLY | O_CREAT, 755);
		
	getcwd(dirPath, 32);
	
	printf("%s/%s\n",dirPath,dirName);
	 return 0;
}
