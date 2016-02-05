# coding=utf-8
'''
Created on Feb 4, 2016

@author: yangjie
'''
import pygraphviz

from uml_graphviz.setting.logger import uml_logger


class UMLElement(object):

    def __init__(self, element_name: str, element_shape: str, element_style: str):
        self.element_name = element_name
        self.element_shape = element_shape
        self.element_style = element_style

    def get_label(self):
        name_str = self.element_name
        label_str = name_str
        uml_logger.info("get label %s" % (self.element_name,))
        return label_str


class UMLOneElement(UMLElement):

    def __init__(self, element_name: str, element_shape: str, element_style: str):
        super(UMLOneElement, self).__init__(
            element_name, element_shape, element_style)


class UMLTwoElement(UMLElement):

    def __init__(self, element_name: str, element_name_start: str, element_name_end: str):
        super(UMLTwoElement, self).__init__(element_name)
        self.element_name_start = element_name_start
        self.element_name_end = element_name_end


class UMLFigure(pygraphviz.AGraph):

    def __init__(self, strict: bool=True, directed: bool=False):
        uml_logger.info("create uml figure")

    def draw_uml(self, file_name: str):
        self.layout("dot")
        self.draw(file_name)
        uml_logger.info("draw uml figure %s" % (file_name,))

    def add_uml_element(self, element: UMLElement):
        if isinstance(element, UMLOneElement):
            self._add_one_element(element)
        elif isinstance(element, UMLTwoElement):
            self.add_two_element(element)
        else:
            uml_logger.error("unknown type")

    def _add_one_element(self, element: UMLOneElement):
        self.add_node(element.element_name, label=element.get_label(
        ), shape=element.element_shape, style=element.element_style)

    def _add_two_element(self, element: UMLTwoElement):
        pass
