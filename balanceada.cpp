#include<iostream>
#include<stack>
#include<string>
using namespace std;

bool balanco(const string& expressao){
	stack<char>pilha;
	
	for(int i=0;i<sizeof(expressao);i++){  //embarcadero
		if(expressao[i]=='('){
			pilha.push(expressao[i]);
			
		}
		else if (expressao[i]==')'){
			if(pilha.empty()){
				return false;
			}
			pilha.pop();// se pilha não vazia e ')' desempilha
		}
		return pilha.empty();	
	}
}
 int main(){
 	string str;
 	cout<<"Digite a espressao "<<endl;
 	getline(cin,str);
 	if (balanco(str)){
 		cout<<" expressao balanceada "<<endl;
	 }
	 else {
	 	cout<<" expressao nao balanceada "<<endl;
	 }
 }
	
