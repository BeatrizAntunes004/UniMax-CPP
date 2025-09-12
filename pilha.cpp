#include<iostream>
#include<stack>
#include<cstdlib>
#include<ctime>
using namespace std; 

int main(){
	
	stack<int>pilha;
	srand(time(NULL));
	
	/*pilha.push(10);
	pilha.push(20);
	pilha.push(30);*/
	
	for(int i=1;i<=10;i++){
		int ale = rand()%21;//gera no.s aleatórios de 0a 20
		pilha.push(ale);
		cout<<"Pilha ["<<i<<"] = "<<pilha.top()<<endl;
		
	}
	
	cout <<" Tamanho da pilha "<<pilha.size()<<endl;
	cout <<" Topo da pilha = "<<pilha.top()<<endl;
	
	while(!pilha.empty()){
	pilha.pop();	
	}
	
	cout<<endl;
    cout <<"Tamanho da pilha  "<<pilha.size()<<endl;
	cout <<"Topo da pilha   "<<pilha.top()<<endl;
}
