#include <iostream>

using namespace std;

void soma(int n){
	int s, i;
	i=n;
	while(i>=1){
		s+=i;
		cout<<i<< " ";
		i--;
		
	}
	cout <<"Somatorio = "<<s;
}
int main(){
	int num;
	cout<<"Digite o numero ";
	cin >> num;
	soma(num);
	
	return 0;
}
