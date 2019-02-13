#include <iostream>
#include <vector>

using namespace std;


// finds the sum of the multiples of 3, 5 up to a number
int find_sum_multiples(int number){

	// initialize sum of multiples
	int sum = 0;

	// vectors for storing multiples
	vector<int> multiples;

	// loop through all numbers up to number
	for(int i=1; i<number; i++){
		if(i%3 == 0){
			multiples.push_back(i);
		}else if(i%5 == 0){
			multiples.push_back(i);
		}
	}

	// sum multiples
	for(int j=0; j<=multiples.size(); j++){
		sum = sum + multiples[j];
	}
	
	return sum;
}


int main(){
	cout<<find_sum_multiples(1000)<<endl;
	return 0;
}