#include <iostream>
#include <vector>

using namespace std;


int find_nth_prime(int n, int max_num){
	
	// init variables
	vector<int> primes;
	primes.push_back(2);
	
	// main search loop
	for(int num=3; num <= max_num; num++){

		// check to see if n was reached
		if (primes.size()==n){
			break;
		}

		// set condition
		bool is_prime = 1;

		// loop through primes
		for(int i=1; i<=primes.size(); i++){

			// check if divisable
			if(num%primes[i-1] == 0){
				is_prime = 0;
				break;
			}

		}

		if(is_prime){
			primes.push_back(num);
		}

	}

	return primes[n-1];
}

int main(){
	cout<<find_nth_prime(10001, 999999)<<endl;
	return 0;
}