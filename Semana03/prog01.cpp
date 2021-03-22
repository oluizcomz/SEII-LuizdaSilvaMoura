#include <iostream>
#include "Complexo.h"


int main(){
    
    Complexo num(1.0,2.0);
    Complexo num1;
    Complexo num2(2.0,3.0);//
    Complexo num3;
    Complexo num4;
    Complexo num5;
   
    
    cout<<"\nnum1 = num1 - (1 +1i)\n num1 :"<<endl;
    num1 = num1.Sub(1,1);
    num1.GetRet();
    num1.GetPol();
    
    cout<<"\nnum2 : "<<endl;
    num2.GetRet();

    cout<<"\nnum3 = num1 + num2\n num3 :"<<endl; 
    num3 = num1.Soma(num2);
    num3.GetRet();
    
    cout<<"\nnum4 = num/num \n num4 :"<<endl; 
    num4 = num.Div(num3);
    num4.GetPol();
    
    
    cout<<"\nnum5 = num1 *num4\n num5: "<<endl; 
    num5 = num1.Mult(num4); 
    num5.GetRet();
    num5.GetPol();
    
    return 0;
}