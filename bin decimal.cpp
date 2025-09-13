#include <iostream>
#include <stack>
#include <cmath>

using namespace std;
int Bin_Dec(string numero){
	stack<char>pilha;
	for(size_t  i=0;i<numero.size (); i++){
		if (numero[i]=='0'||numero[i] == '1'){
			pilha.push(numero[i] -'0' );//transforma de char para int
		}
		else{
			cout<<"Numero invalido: ";
			return 1;
		}
	}
	int dec = 0;
	int exp = 0;
	while(!pilha.empty()){
		int bit = pilha.top();
		pilha.pop();
		dec += bit*pow(2,exp);
		exp++;
	}
	return dec;
	
	}

int main(){
	string bin;
	cout<<"Informe o numero binario: ";
	cin>>bin;
	cout<<"Decimal: "<<Bin_Dec(bin)<<endl;
}
