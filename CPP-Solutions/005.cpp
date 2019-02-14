// what number is evenly divisable by
// all numbers between 1 and 20

# include <iostream>
# include <vector>
# include <math.h>

using namespace std;

// determines whether or not number is prime
bool is_prime(long long int number){

	// making upper bound for search
	// setting prime status
	bool is_prime = 1;
	long double root_num = sqrt(number);
	long long int upper_bound = static_cast<long long int>(root_num);

	// searches to upper bound do find a divisor
	for(int i=2; i<=upper_bound; i++){
		if (number == 2){
			return 1;
		}

		if(number%i == 0){
			is_prime = 0;
			break;
		}
	}

	return is_prime;
}


// find the first number evenly divisable by all
// integers up to the value x
int evenly_divisable(int x){
	// initiate vector
	vector<long long int> divisors;
	bool condition;

	// fill vector with 0's
	for(long long int i=0; i <= x; i++){
		divisors.push_back(0);
	}

	// find lowest common factors
	// of each int an multiply together
	// gives the lowest number possible
	for(int i=1; i <= x+1; i++){
		for(int j=2; j <= x; j++){
			bool condition = 1;
			int holder = i;
			int divides = 0;
			while(condition){
				if(holder % j == 0){
					divides = divides + 1; 
					holder = holder / j;
					
				}else{
					condition=0;
				}
			}
			if((divides > divisors[j]) && (is_prime(j))){
				divisors[j] = divides;
			}
		}
	}

	// power and then multiply each number
	int number = 1;
	for(int i=1; i<= x+1; i++){
		number = number * pow(i, divisors[i]);
	}


	return number;
}

int main(){
	cout<<evenly_divisable(20)<<endl;

}





