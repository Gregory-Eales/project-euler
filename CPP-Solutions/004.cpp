#include <iostream>
#include <string>

using namespace std;


int largest_palindrome(){

	for(int i=0; i<1000; i++){
		for(int j=0;i<1000; j++){
			break;
		}
	}
	return 0;
}


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
			if(num.at(i) != num.at(num_length - i)){
				is_palindrome = 0;
				break;
			}
	}

	return is_palindrome;
}



int main(){
	int x = 3331333;
	string x_string = to_string(x);
	cout<<x_string.at(1)<<endl;
	return 0;
}