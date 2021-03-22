#include <stdlib.h>
#include "cp.h"
int main(int argc, char const *argv[])
{
    char *str;
    int tamanho = strlen("cp");
    str = malloc ((tamanho+1) * sizeof (char));
    strcpy(str, "cp");
    for (int i = 1; i < argc; i++)
    {
        tamanho = strlen(argv[i]) + tamanho;
        str = realloc (str, (tamanho+2) * sizeof (char));
        strcat(str, " ");
        strcat(str, argv[i]);
        
    }
    cpRedirector(str);
    free(str);
    return 0;
}

