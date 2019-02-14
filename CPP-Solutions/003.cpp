#include <iostream>
#include <math.h>

using namespace std;

// determines whether or not number is prime
bool is_prime(long long int number){

	// making upper bound for search
	// setting prime status
	bool is_prime = 1;
	long double root_num = sqrt(number);
	long long int upper_bound = 1 + static_cast<long long int>(root_num);

	// searches to upper bound do find a divisor
	for(int i=2; i<=upper_bound; i++){
		if(number%i == 0){
			is_prime = 0;
			break;
		}
	}

	return is_prime;
}

// gets the largest prime factor of a number
long long int largest_prime_factor(long long int number){
	// upper bound and placeholder
	long long int upper_bound = 1 + static_cast<long long int>(sqrt(number));
	long long int prime_factor = 0;

	// searches to upper bound to find highest prime multiple
	for(int i=2; i<=upper_bound; i++){
		if(number%i == 0){
			if(is_prime(i)){
				prime_factor = i;
			}
		}
	}

	return prime_factor;
}

int main(){
	long long int number = 600851475143;
	cout<<largest_prime_factor(number)<<endl;
	return 0;
}