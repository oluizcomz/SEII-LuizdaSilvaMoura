#ifndef _COMPLEXO_H_
#define _COMPLEXO_H_

#include <cmath>
#include <iostream>
using namespace std;

class Complexo
{
    private:
    double modulo, fase;
    double real, imaginario;
    void PolforRet();
    void RetforPol();
    public:
    
    Complexo();
    Complexo(double real, double img);
    Complexo Div(Complexo& b);
    Complexo Div(double modulo,double fase);
    void GetPol();
    void GetRet();
    double GetRea();
    double GetImg();
    double GetMod();
    double GetFas();
    Complexo Mult(double real, double img);
    Complexo Mult(Complexo& b);
    double *PolforRet(double mod, double fas);
    double *RetforPol(double real, double imaginario);
    void SetPol(double modulo, double fase);
    void SetRet(double real, double imaginario);
    Complexo Soma(double real, double img);
    Complexo Soma(Complexo& b);
    Complexo Sub(Complexo& b);
    Complexo Sub(double real, double img);
    
    
    
};

#endif