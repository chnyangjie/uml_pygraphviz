# coding=utf-8
'''
Created on Feb 5, 2016

@author: yangjie
'''
from uml_graphviz.uml_blocks.umlBaseElement import UMLFigure


class UMLFigure_Usual(UMLFigure):

    def __init__(self, strict: bool=True, directed: bool=False):
        super(UMLFigure, self).__init__(strict=strict, directed=directed)
