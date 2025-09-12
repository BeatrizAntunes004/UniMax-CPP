#include <iostream>
using namespace std;

int soma_vet(int v [], int tamanho){
	if (tamanho == 0)
		return 0;
	else 
		retun v [tamanho-1]+soma_vet(v,tamanho-1);
	
	}
	int main()[
	int v[] = {1,2,3,4,5};
	int tamanho = sizeof(v)/sizeof(v[0]);
	cout<< "Soma = " <<soma_vet(v, tamanho)<< endl;
	
	return 0;
	
	]

