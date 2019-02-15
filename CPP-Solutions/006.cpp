#include <iostream>
#include <math.h>

using namespace std;


// find the difference between the sum of
// the squares and the square of the sum
long long int diff_sum_sqr(long long int x){
	
	// init variables
	long long int square_sum = 0;
	long long int sum_square = 0;
	
	// loop throught ints
	// calculate variables
	for(long long int i=1; i <= x; i++){
		sum_square = sum_square + pow(i, 2);
		square_sum = square_sum + i;
	}

	square_sum = pow(square_sum, 2);

	return square_sum - sum_square;
}



int main(){
	cout<<diff_sum_sqr(100)<<endl;
	return 0;
}