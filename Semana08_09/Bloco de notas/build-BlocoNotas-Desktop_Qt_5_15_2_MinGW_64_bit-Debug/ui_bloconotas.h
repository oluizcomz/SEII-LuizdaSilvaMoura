/********************************************************************************
** Form generated from reading UI file 'bloconotas.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BLOCONOTAS_H
#define UI_BLOCONOTAS_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_BlocoNotas
{
public:
    QAction *actionAbrir;
    QAction *actionNovo;
    QAction *actionSalvar;
    QAction *actionSalvar_Como;
    QAction *actionFechar;
    QAction *actionCopiar;
    QAction *actionRecortar;
    QAction *actionColar;
    QAction *actionDesfazer;
    QAction *actionRefazer;
    QAction *actioninfo;
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QTextEdit *textEdit;
    QMenuBar *menubar;
    QMenu *menuArquivo;
    QMenu *menuEditar;
    QMenu *menuSobre;
    QToolBar *toolBar;

    void setupUi(QMainWindow *BlocoNotas)
    {
        if (BlocoNotas->objectName().isEmpty())
            BlocoNotas->setObjectName(QString::fromUtf8("BlocoNotas"));
        BlocoNotas->resize(900, 900);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(BlocoNotas->sizePolicy().hasHeightForWidth());
        BlocoNotas->setSizePolicy(sizePolicy);
        BlocoNotas->setMinimumSize(QSize(0, 0));
        BlocoNotas->setSizeIncrement(QSize(400, 400));
        BlocoNotas->setBaseSize(QSize(400, 400));
        BlocoNotas->setStyleSheet(QString::fromUtf8("*{\n"
"  	font-weight: 500;\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"QToolBar, QTextEdit{\n"
"	border: none;\n"
"}\n"
" QTextEdit{\n"
"	padding: 10%;\n"
"	color: rgb(235, 235, 235);\n"
"	background-color: rgb(60, 60, 60);\n"
"}"));
        actionAbrir = new QAction(BlocoNotas);
        actionAbrir->setObjectName(QString::fromUtf8("actionAbrir"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icones/icones/abrir.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionAbrir->setIcon(icon);
        actionNovo = new QAction(BlocoNotas);
        actionNovo->setObjectName(QString::fromUtf8("actionNovo"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icones/icones/new.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionNovo->setIcon(icon1);
        actionSalvar = new QAction(BlocoNotas);
        actionSalvar->setObjectName(QString::fromUtf8("actionSalvar"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icones/icones/save.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionSalvar->setIcon(icon2);
        actionSalvar_Como = new QAction(BlocoNotas);
        actionSalvar_Como->setObjectName(QString::fromUtf8("actionSalvar_Como"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icones/icones/salvarcomo.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionSalvar_Como->setIcon(icon3);
        actionFechar = new QAction(BlocoNotas);
        actionFechar->setObjectName(QString::fromUtf8("actionFechar"));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icones/icones/cancel.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionFechar->setIcon(icon4);
        actionCopiar = new QAction(BlocoNotas);
        actionCopiar->setObjectName(QString::fromUtf8("actionCopiar"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icones/icones/copy.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionCopiar->setIcon(icon5);
        actionRecortar = new QAction(BlocoNotas);
        actionRecortar->setObjectName(QString::fromUtf8("actionRecortar"));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/icones/icones/recortar.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionRecortar->setIcon(icon6);
        actionColar = new QAction(BlocoNotas);
        actionColar->setObjectName(QString::fromUtf8("actionColar"));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/icones/icones/paste.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionColar->setIcon(icon7);
        actionDesfazer = new QAction(BlocoNotas);
        actionDesfazer->setObjectName(QString::fromUtf8("actionDesfazer"));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/icones/icones/desfazer.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionDesfazer->setIcon(icon8);
        actionRefazer = new QAction(BlocoNotas);
        actionRefazer->setObjectName(QString::fromUtf8("actionRefazer"));
        QIcon icon9;
        icon9.addFile(QString::fromUtf8(":/icones/icones/refazer.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionRefazer->setIcon(icon9);
        actioninfo = new QAction(BlocoNotas);
        actioninfo->setObjectName(QString::fromUtf8("actioninfo"));
        QIcon icon10;
        icon10.addFile(QString::fromUtf8(":/icones/icones/info.png"), QSize(), QIcon::Normal, QIcon::Off);
        actioninfo->setIcon(icon10);
        centralwidget = new QWidget(BlocoNotas);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        textEdit = new QTextEdit(centralwidget);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        QFont font;
        font.setFamily(QString::fromUtf8("Arial"));
        font.setPointSize(14);
        font.setBold(true);
        font.setWeight(62);
        textEdit->setFont(font);

        gridLayout->addWidget(textEdit, 0, 0, 1, 1);

        BlocoNotas->setCentralWidget(centralwidget);
        menubar = new QMenuBar(BlocoNotas);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 900, 21));
        menuArquivo = new QMenu(menubar);
        menuArquivo->setObjectName(QString::fromUtf8("menuArquivo"));
        menuEditar = new QMenu(menubar);
        menuEditar->setObjectName(QString::fromUtf8("menuEditar"));
        menuSobre = new QMenu(menubar);
        menuSobre->setObjectName(QString::fromUtf8("menuSobre"));
        BlocoNotas->setMenuBar(menubar);
        toolBar = new QToolBar(BlocoNotas);
        toolBar->setObjectName(QString::fromUtf8("toolBar"));
        BlocoNotas->addToolBar(Qt::TopToolBarArea, toolBar);

        menubar->addAction(menuArquivo->menuAction());
        menubar->addAction(menuEditar->menuAction());
        menubar->addAction(menuSobre->menuAction());
        menuArquivo->addAction(actionAbrir);
        menuArquivo->addSeparator();
        menuArquivo->addAction(actionSalvar);
        menuArquivo->addAction(actionSalvar_Como);
        menuArquivo->addSeparator();
        menuArquivo->addAction(actionFechar);
        menuEditar->addAction(actionCopiar);
        menuEditar->addAction(actionColar);
        menuEditar->addAction(actionRecortar);
        menuEditar->addSeparator();
        menuEditar->addAction(actionDesfazer);
        menuEditar->addAction(actionRefazer);
        menuSobre->addAction(actioninfo);
        toolBar->addAction(actionNovo);
        toolBar->addAction(actionAbrir);
        toolBar->addSeparator();
        toolBar->addAction(actionSalvar);
        toolBar->addAction(actionSalvar_Como);
        toolBar->addSeparator();
        toolBar->addAction(actionCopiar);
        toolBar->addAction(actionColar);
        toolBar->addAction(actionRecortar);
        toolBar->addSeparator();
        toolBar->addAction(actionDesfazer);
        toolBar->addAction(actionRefazer);
        toolBar->addSeparator();
        toolBar->addAction(actioninfo);
        toolBar->addAction(actionFechar);

        retranslateUi(BlocoNotas);

        QMetaObject::connectSlotsByName(BlocoNotas);
    } // setupUi

    void retranslateUi(QMainWindow *BlocoNotas)
    {
        BlocoNotas->setWindowTitle(QCoreApplication::translate("BlocoNotas", "BlocoNotas", nullptr));
        actionAbrir->setText(QCoreApplication::translate("BlocoNotas", "Abrir", nullptr));
        actionNovo->setText(QCoreApplication::translate("BlocoNotas", "Novo", nullptr));
        actionSalvar->setText(QCoreApplication::translate("BlocoNotas", "Salvar", nullptr));
        actionSalvar_Como->setText(QCoreApplication::translate("BlocoNotas", "Salvar Como", nullptr));
        actionFechar->setText(QCoreApplication::translate("BlocoNotas", "Fechar", nullptr));
        actionCopiar->setText(QCoreApplication::translate("BlocoNotas", "Copiar", nullptr));
        actionRecortar->setText(QCoreApplication::translate("BlocoNotas", "Recortar", nullptr));
        actionColar->setText(QCoreApplication::translate("BlocoNotas", "Colar", nullptr));
        actionDesfazer->setText(QCoreApplication::translate("BlocoNotas", "Desfazer", nullptr));
        actionRefazer->setText(QCoreApplication::translate("BlocoNotas", "Refazer", nullptr));
        actioninfo->setText(QCoreApplication::translate("BlocoNotas", "info", nullptr));
        menuArquivo->setTitle(QCoreApplication::translate("BlocoNotas", "Arquivo", nullptr));
        menuEditar->setTitle(QCoreApplication::translate("BlocoNotas", "Editar", nullptr));
        menuSobre->setTitle(QCoreApplication::translate("BlocoNotas", "Sobre", nullptr));
        toolBar->setWindowTitle(QCoreApplication::translate("BlocoNotas", "toolBar", nullptr));
    } // retranslateUi

};

namespace Ui {
    class BlocoNotas: public Ui_BlocoNotas {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BLOCONOTAS_H
