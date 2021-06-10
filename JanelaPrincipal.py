# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:04:27 2020

@author: Rafae
"""

from PyQt5.QtCore import Qt, pyqtSlot 
from PyQt5.QtWidgets import QMainWindow, QMessageBox , QFileDialog, QDialog, QVBoxLayout, QLabel
from Aplicativo import Ui_JanelaPrincipal
from Api import funcaoGrafico, LinhaBonita

from matplotlib.backends.backend_qt5agg import FigureCanvas,\
                                                NavigationToolbar2QT as NavToolBar

from matplotlib.figure import Figure 


class aplicativo (QMainWindow,Ui_JanelaPrincipal):
    def __init__(self,placeHolder,parent=None,f=Qt.WindowFlags()):
        super(aplicativo,self).__init__(parent,f)
        
        self.setupUi(self)
        self._placeHolder = placeHolder
        self.atualizaPlaceholder()
        self._canvas = FigureCanvas(Figure())
        self._ax = self._canvas.figure.subplots()
        self.centralwidget.layout().addWidget(self._canvas)
        self._ax.set_xlabel("Valor analógico Digital")
        self._ax.set_ylabel("Valor Real da grandeza")
        self._ax.set_title('Função Polinomial',fontweight= "bold", fontsize="20")
        self._barra = NavToolBar(self._canvas,self)
        self.centralwidget.layout().addWidget(self._barra)
        self._ax.grid()
        self._plot1 = None
        self._plot2 = None
        
    def atualizaPlaceholder(self):
        self.label.setText(self._placeHolder)
        
          
    @pyqtSlot()
    def on_actionSair_triggered(self):
        if QMessageBox.question(self,"Confirmar Fim",
                               "Deseja sair do aplicativo?") == QMessageBox.Yes: self.close()
    
    @pyqtSlot()
    def on_actionAbrir_triggered(self):
        self.fileName = QFileDialog.getOpenFileName(self, 'Open file', 
        'c:\\',"Text files (*.csv)")        
        self._placeHolder = (LinhaBonita((funcaoGrafico(self.fileName[0]))[0]))
        self.atualizaPlaceholder() 
        self.VRO = ((((funcaoGrafico(self.fileName[0]))[2])[0]))
        self.ADO = ((((funcaoGrafico(self.fileName[0]))[1])[0]))
        self.plotGrafico()
        
    @pyqtSlot()   
    def on_actionSobre_triggered(self):
        modal = QDialog()
        
        modal.setMinimumSize(300,300)

        VB = QVBoxLayout()
        modal.setLayout(VB)

        Label1 = QLabel("Nome: Rafael Huszcza Machado", modal)
        Label1.setStyleSheet('QLabel { background-color: "#000"; color: "#fff"; font-size: 20px}')
        VB.addWidget(Label1)
        
        Label2 = QLabel("Turma: 4E", modal)
        Label2.setStyleSheet('QLabel { background-color: "#000"; color: "#fff"; font-size: 20px}')
        VB.addWidget(Label2)
        
        Label3 = QLabel("Matrícula: 11050274", modal)
        Label3.setStyleSheet('QLabel { background-color: "#000"; color: "#fff"; font-size: 20px}')
        VB.addWidget(Label3)
        
        Label4 = QLabel("Disciplina: Informática Industrial", modal)
        Label4.setStyleSheet('QLabel { background-color: "#000"; color: "#fff"; font-size: 20px}')
        VB.addWidget(Label4)
        
        Label5 = QLabel("O que o programa faz:\n o programa faz a leitura de um arquivo csv e a partir dos dados lidos \n o mesmo cria uma função polinomial e faz um gráfico ", modal)
        Label5.setStyleSheet('QLabel { background-color: "#000"; color: "#fff"; font-size: 10px}')
        VB.addWidget(Label5)
        
        modal.exec_()
           
    def plotGrafico(self):
        if self._plot1 is None and self._plot2 is None:            
            self._plot1 = self._ax.plot(((funcaoGrafico(self.fileName[0]))[3]),((funcaoGrafico(self.fileName[0]))[4]), color='red', label='Função Polinomial')[0]
            self._plot2 = self._ax.plot(((funcaoGrafico(self.fileName[0]))[5]),((funcaoGrafico(self.fileName[0]))[6]), "ro",color='green', label='Valores medidos pelo sensor')[0]          
        else:
            self._ax.clear()   
            self._ax.set_xlabel("Valor analógico Digital")
            self._ax.set_ylabel("Valor Real da grandeza")
            self._ax.set_title('Função Polinomial',fontweight= "bold", fontsize="20")
            self._ax.grid()                 
            self._plot1 = self._ax.plot(((funcaoGrafico(self.fileName[0]))[3]),((funcaoGrafico(self.fileName[0]))[4]), color='red', label='Função Polinomial')[0]
            self._plot2 = self._ax.plot(((funcaoGrafico(self.fileName[0]))[5]),((funcaoGrafico(self.fileName[0]))[6]), "ro",color='green', label='Valores medidos pelo sensor')[0]
        self._ax.legend(loc='lower right')   
        self._canvas.draw()
        
       