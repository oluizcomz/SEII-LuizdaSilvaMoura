#ifndef BLOCONOTAS_H
#define BLOCONOTAS_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class BlocoNotas; }
QT_END_NAMESPACE

class BlocoNotas : public QMainWindow
{
    Q_OBJECT

public:
    BlocoNotas(QWidget *parent = nullptr);
    ~BlocoNotas();

private slots:
    void on_actionNovo_triggered();

    void on_actionAbrir_triggered();

    void on_actionSalvar_Como_triggered();

    void on_actionSalvar_triggered();

    void on_actionFechar_triggered();

    void on_actionCopiar_triggered();

    void on_actionRecortar_triggered();

    void on_actionColar_triggered();

    void on_actionDesfazer_triggered();

    void on_actionRefazer_triggered();

private:
    Ui::BlocoNotas *ui;
    QString local_arquivo;
};
#endif // BLOCONOTAS_H
