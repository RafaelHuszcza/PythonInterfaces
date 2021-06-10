# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:09:29 2020

@author: Rafae
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

from JanelaPrincipal import aplicativo

#from Api import 

if __name__=="__main__":
    app = QApplication(sys.argv)
    
    janela = aplicativo("Polinomio")
    janela.show()
    
    app.exec_()
