#include <iostream>
using namespace std;

int fatorial (int n){
	 if (n == 0)
	 	return 1;
	 else
	 return n * fatorial (n-1);
}
int main(){
	int i, n;
	cout<<"Digite um numero ";
	cin>> n;
	cout<<"Fatorial = "<<fatorial(n)<<endl;
	return 0;
}
