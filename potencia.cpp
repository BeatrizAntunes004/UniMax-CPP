#include <iostream>

using namespace std;
int potencia (int base, int expo){
	 if (expo == 0)
	 	return 1;
	 else
	 return base * potencia(base, expo-1);//hipotese
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
