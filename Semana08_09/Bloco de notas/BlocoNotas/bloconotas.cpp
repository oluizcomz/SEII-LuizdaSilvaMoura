#include "bloconotas.h"
#include "ui_bloconotas.h"
#include <QMessageBox>
#include <QFile>
#include<QFileDialog>
#include <QTextStream>

BlocoNotas::BlocoNotas(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::BlocoNotas)
{
    ui->setupUi(this);
    this->setCentralWidget(ui->textEdit);
}

BlocoNotas::~BlocoNotas()
{
    delete ui;
}


void BlocoNotas::on_actionNovo_triggered()
{
    local_arquivo = "";
    ui->textEdit->clear();
    ui->textEdit->setFocus();
}

void BlocoNotas::on_actionAbrir_triggered()
{
    QString filtro = " Arquivos de Texto (*.txt) ;;Todos os Arquivos (*.*)";
    QString nome_arquivo =QFileDialog::getOpenFileName(this,"Abrir",QDir::homePath(),filtro);
    QFile arquivo(nome_arquivo);
    local_arquivo = nome_arquivo;
    if(!arquivo.open(QFile::ReadOnly | QFile::Text)){
        QMessageBox::warning(this,"","Arquivo não pode ser aberto");
        return;
    }
    QTextStream entrada (&arquivo);
    QString texto =entrada.readAll();
    ui->textEdit->setText(texto);
    arquivo.close();
}

void BlocoNotas::on_actionSalvar_Como_triggered()
{
    QString filtro = " Arquivos de Texto (*.txt) ;;Todos os Arquivos (*.*)";
    QString nome_arquivo =QFileDialog::getSaveFileName(this,"Salvar como",QDir::homePath(),filtro);
    QFile arquivo(nome_arquivo);
    local_arquivo = nome_arquivo;
if(!arquivo.open(QFile::WriteOnly | QFile::Text)){
        QMessageBox::warning(this,"","Arquivo não pode ser salvo");
        return;
    }
    QTextStream saida(&arquivo);
    QString texto =ui->textEdit->toPlainText();
    saida << texto;
    arquivo.flush();
    arquivo.close();

}

void BlocoNotas::on_actionSalvar_triggered()
{
    QFile arquivo(local_arquivo);
   if(!arquivo.open(QFile::WriteOnly | QFile::Text)){
        QMessageBox::warning(this,"","Arquivo não pode ser salvo");
        return;
    }
    QTextStream saida(&arquivo);
    QString texto =ui->textEdit->toPlainText();
    saida << texto;
    arquivo.flush();
    arquivo.close();
}

void BlocoNotas::on_actionFechar_triggered()
{
    close();
}

void BlocoNotas::on_actionCopiar_triggered()
{
    ui->textEdit->copy();
}

void BlocoNotas::on_actionRecortar_triggered()
{
    ui->textEdit->cut();
}

void BlocoNotas::on_actionColar_triggered()
{
     ui->textEdit->paste();
}

void BlocoNotas::on_actionDesfazer_triggered()
{
    ui->textEdit->undo();
}

void BlocoNotas::on_actionRefazer_triggered()
{
     ui->textEdit->redo();
}
