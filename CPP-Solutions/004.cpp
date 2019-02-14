#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool is_palindrome(int number){
	bool is_palindrome = 1;
	string num = to_string(number);
	int num_length = num.length();

	// if num length is even
	if(num_length % 2 == 0){
		for(int i=0; i<= num_length/2; i++){
			if(num.at(i) != num.at(num_length - 1 - i)){
				is_palindrome = 0;
				break;
			}
		}

	}else{
		for(int i=0; i<= (num_length - 1)/2; i++){
			if(num.at(i) != num.at(num_length - 1 - i)){
				is_palindrome = 0;
				break;
			}
		}
	}

	return is_palindrome;
}

int largest_palindrome(){

	for(int depth=1; depth<100;depth++){
		cout<<depth<<endl;
		for(int i=0; i<depth; i++){
			int x = 1000 - i;
			for(int j=0;j<30; j++){
				int y = 1000 - j;
				if(is_palindrome(x*y)){
					return x*y;
				}
			}
		}
	}

	
	return 0;
}


int main(){
	cout<<largest_palindrome()<<endl;
	return 0;
}