#include "common.h"

int main(){
	
	print("첫번째 숫자 입력 : ");
	int oneint = inputInt();
	
	print("두번째 숫자 입력 : ");
	int twoint = inputInt();
	
	printInt(oneint + twoint);
	
	print("\n");
	
	return 0;
}

