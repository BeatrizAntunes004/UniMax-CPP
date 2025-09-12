#include<iostream>
 
 using namespace std;
 
int ContarCaracteres(const char* str){
	int cont = 0;
	int i=0;
	while(*str != '\0'){
		if(!isspace(*str)&&!isdigit(*str)&&!ispunct(*str))
		cont ++;
		str++;
	}
	return(cont); 
}
void gera_int(int *vet, int d, int inicio, int final){
	
}
void gera_float(float *vet, int d, float inicio, float final){
}

int main () {
	const char * texto = "Sexta-feira";
	cout<< ContarCaracteres(texto);
	
	return 0;
}
 
