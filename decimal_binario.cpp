#include <iostream>
#include <stack>

using namespace std;

void Dec_Bin(int numero){
	stack<int>pilha;
	if (numero == 0){
	
	cout<<"0";
}

while(numero >0){
	pilha.push(numero%2);
	numero/=2;
}
cout<<"Binario: ";
while(!pilha.empty()){
	cout<<pilha.top();
	pilha.pop();
}

}

int main(){
	int num;
	cout<<"Informe o numero inteiro:  ";
	cin>>num;
	cout<<"Decimal:  "<<num<<endl;
	Dec_Bin(num);
	return 0;
}
