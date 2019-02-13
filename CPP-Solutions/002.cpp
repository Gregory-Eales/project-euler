#include <iostream>

using namespace std;

// finds the sum of the even fibonacci numbers up to x
int sum_even_fibonacci(int x){

	// summ of even fibonacci numbers
	int sum = 0;

	// initiating fibonacci numbers
	int prev_fib = 1;
	int fib = 1;
	int post_fib = 0;

	// condition statement
	bool summing = 1;

	// loop until x is reached
	while(summing){
		if(fib%2 == 0){
			sum = sum + fib;
		}

		// get next fib num in the sequence
		post_fib = prev_fib + fib;
		prev_fib = fib;
		fib = post_fib;

		// check to see if loop has reached x
		if(fib > x){
			summing = 0;
		}
	}

	return sum;

}

int main(){
	cout<<sum_even_fibonacci(4000000)<<endl;
	return 0;
}