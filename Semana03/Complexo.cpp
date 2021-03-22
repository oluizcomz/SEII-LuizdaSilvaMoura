
#include "Complexo.h"

Complexo ::Complexo()
{
    this->real = 0.0;
    this->imaginario = 0.0;
    this->modulo = 0.0;
    this->fase = 0.0;
}
Complexo ::Complexo(double real, double img)
{
    this->real = real;
    this->imaginario = img;
    RetforPol();
}
Complexo Complexo::Div(Complexo &b)
{
    double m = this->modulo / b.GetMod();
    double f = this->fase - b.GetFas();
    double *conv;
    conv = PolforRet(m, f);
    Complexo util(conv[0], conv[1]);
    return util;
}
Complexo Complexo::Div(double modulo, double fase)
{
    double m = this->modulo / modulo;
    double f = this->fase - fase;
    double *conv;
    conv = PolforRet(m, f);
    Complexo util(conv[0], conv[1]);
    return util;
}
void Complexo::GetRet()
{
    cout << "Ret:" << this->real << "+" << this->imaginario << "j" << endl;

}
void Complexo::GetPol()
{
    cout << "Pol:" << this->modulo << "<" << this->fase << "°" << endl;
}
double Complexo::GetRea()
{
    return this->real;
}
double Complexo::GetImg()
{
    return this->imaginario;
}
double Complexo::GetMod()
{
    return this->modulo;
}
double Complexo::GetFas()
{
    return this->fase;
}
Complexo Complexo::Mult(double real, double img)
{
    double i = (real * this->real) - (img * this->imaginario);
    double j = (real * this->imaginario) + (img * this->real);
    Complexo util(i, j);
    return util;
}
Complexo Complexo::Mult(Complexo &b)
{
    double i = (b.GetRea() * this->real) - (b.GetImg() * this->imaginario);
    double j = (b.GetRea() * this->imaginario) + (b.GetImg() * this->real);
    Complexo util(i, j);
    return util;
}
void Complexo::PolforRet()
{
    this->real = this->modulo * cos(this->fase * M_PI / 180.0);
    this->imaginario = this->modulo * sin(this->fase * M_PI / 180.0);
}
double *Complexo::PolforRet(double mod, double fas)
{
    double util[2];
    double *p;
    p = util;
    util[0] = mod * cos(fas * M_PI / 180.0);
    util[1] = mod * sin(fas * M_PI / 180.0);

    return p;
}
double *Complexo::RetforPol(double real, double imaginario)
{
    double util[2];
    double *p;
    util[0] = hypot(real, imaginario);
    if (real == 0.0 && imaginario != 0.0)
        util[1] = 90.0;
    else if (real != 0.0)
        util[1] = atan(imaginario / real) * 180.0 / M_PI;

    if ((imaginario <= 0.0 && real <= 0.0) || (imaginario >= 0.0 && real < 0.0))
    {
        if (imaginario == 0.0 && real == 0.0)
            util[1] = 0.0;
        else
            util[1] = util[1]+ 180.0;
    }
    p = util;
    return p;
}
void Complexo::RetforPol()
{
    this->modulo = hypot(this->real, this->imaginario);
    if (this->real == 0.0 && this->imaginario != 0.0)
        this->fase = 90.0;
    else if (this->real != 0.0)
        this->fase = atan(this->imaginario / this->real) * 180.0 / M_PI;

    if ((this->imaginario <= 0.0 && this->real <= 0.0) || (this->imaginario >= 0.0 && this->real < 0.0))
    {
        if (this->imaginario == 0.0 && this->real == 0.0)
            this->fase = 0.0;
        else
            this->fase = this->fase + 180.0;
    }
}
void Complexo::SetPol(double modulo, double fase){
    this->modulo = modulo;
    this->fase = fase;
    PolforRet();
}
void Complexo::SetRet(double real, double imaginario){
    this->real = real;
    this->imaginario = imaginario;
    PolforRet();
}
Complexo Complexo::Soma(double real, double img)
{
    double i = real + this->real;
    double j = img + this->imaginario;
    Complexo util(i, j);
    return util;
}
Complexo Complexo::Soma(Complexo &b)
{
    double i = b.GetRea() + this->real;
    double j = b.GetImg() + this->imaginario;
    Complexo util(i, j);
    return util;
}
Complexo Complexo::Sub(Complexo &b)
{
    double i = -b.GetRea() + this->real;
    double j = -b.GetImg() + this->imaginario;
    Complexo util(i, j);
    return util;
}
Complexo Complexo::Sub(double real, double img)
{
    double i = -real + this->real;
    double j = -img + this->imaginario;
    Complexo util(i, j);
    return util;
}
