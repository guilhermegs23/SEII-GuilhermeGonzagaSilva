/*Programa 2 
  Guilherme Gonzaga Silva
  11621EMT021
*/

#include <stdlib.h>
#include <stdio.h>


int copyPaste(char *arquivo_antigo, char *arquivo_novo){
	FILE *copy,*colar;
	copy = fopen(arquivo_antigo, "r");
	colar = fopen(arquivo_novo, "w"); 
	int ch;
  	
    while ((ch = getc (copy)) != EOF){
       putc (ch, colar);
    }
    
    fclose(copy);
    fclose(colar);
}

int main(int argc, char *argv[]){
    
    char *a, *b;
    int dim = 0;
    a = malloc ((dim + 1) * sizeof(char));
    b = malloc ((dim + 1) * sizeof(char));
    dim = alen(argv[1]);
    a = realloc(a, (dim + 1) * sizeof(char));
    acat(a, argv[1]);
    dim = alen(argv[2]);
    b = realloc (b, (dim + 1) * sizeof(char));
    acat(b, argv[2]);
    printf("\n%s\n", a);
    printf("\n%s\n", b);
    copyPaste(a, b);
    free(a);
    free(b);
    return 0;
}