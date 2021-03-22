#include <stdio.h>
#include <stdlib.h> 
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int main(int argc, char **argv)
{
    int n,retirar, Colocar,mov;
    ofstream out("Rprog03.txt");

    if (argc > 1)
        n = atoi(argv[1]);
    else
        n = 3;

    for (mov = 1; mov < (1 << n); mov++)
    {
        retirar = (mov & (mov - 1)) % 3 + 1;
        Colocar = ((mov | (mov - 1)) + 1) % 3 + 1;

        cout << "Mova o disco da torre " <<retirar << " para a torre "<<Colocar<<endl; 
        out << "Mova o disco da torre " <<retirar << " para a torre "<<Colocar<<endl;
	    
    }
    mov--;
    out<<"Total de movimentos: "<<mov<<endl;
    out.close();
    return 0;
}
