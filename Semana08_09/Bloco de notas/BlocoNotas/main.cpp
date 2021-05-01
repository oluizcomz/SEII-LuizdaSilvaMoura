#include "bloconotas.h"


#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    BlocoNotas w;
    w.show();
    return a.exec();
}
