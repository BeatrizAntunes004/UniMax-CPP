#include <iostream>
using namespace std;

int potencia (int b, int a){
	int pot, i;
    pot = 1;
    while(i<=a){
    	pot *=b;
    	i++;
	}
	return pot;
}
int main(){
	int base, expo,p;
	cout<<"Digite a base ";
	cin>> base;
	cout<<"Digite o expoente ";
	cin>> expo;
	p = potencia(base,expo);
	cout<<base<<" elevado a "<< expo<<" = "<<p<<endl;
	
	return 0;
}

