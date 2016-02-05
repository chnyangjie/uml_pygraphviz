# coding=utf-8
'''
Created on Feb 4, 2016

@author: yangjie
'''
from uml_graphviz.setting.logger import uml_logger
from uml_graphviz.uml_blocks.umlBaseElement import UMLOneElement


class UMLClass(UMLOneElement):

    def __init__(self, element_name: str, element_attribute: list, element_operation: list, element_shape="record", element_style="solid"):
        super(UMLClass, self).__init__(
            element_name, element_shape, element_style)
        self.element_attribute = element_attribute
        self.element_operation = element_operation

    def get_label(self):
        element_name_str = self.element_name
        element_attribute_str = "\l".join(self.element_attribute)
        element_operation_str = "\l".join(self.element_operation)
        label_str = "{%s|%s|%s}" % (
            element_name_str, element_attribute_str, element_operation_str)
        uml_logger.info("get class label %s" % (self.element_name,))
        return label_str


class UMLInterface(UMLOneElement):

    def __init__(self, element_name: str, element_operation, element_shape="record", element_style="solid"):
        super(UMLInterface, self).__init__(
            element_name, element_shape, element_style)
        self.element_operation = element_operation

    def get_label(self):
        element_name_str = self.element_name
        element_operation_str = "\l".join(self.element_operation)
        label_str = "{%s|%s}" % (element_name_str,  element_operation_str)
        uml_logger.info("get interface label %s" % (self.element_name,))
        return label_str


class UMLCollaboration(UMLOneElement):

    def __init__(self, element_name: str, element_shape="ellipse", element_style="dashed"):
        super(UMLCollaboration, self).__init__(
            element_name, element_shape, element_style)


class UMLUseCase(UMLOneElement):

    def __init__(self, element_name: str, element_shape="ellipse", element_style="solid"):
        super(UMLUseCase, self).__init__(
            element_name, element_shape, element_style)


class UMLComponent(UMLOneElement):

    def __init__(self, element_name: str, element_shape="component", element_style="solid"):
        super(UMLComponent, self).__init__(
            element_name, element_shape, element_style)


class UMLNode(UMLOneElement):

    def __init__(self, element_name: str, element_shape="box3d", element_style="solid"):
        super(UMLNode, self).__init__(
            element_name, element_shape, element_style)


class UMLStateMachine(UMLOneElement):

    def __init__(self, element_name: str, element_shape="Mrecord", element_style="solid"):
        super(UMLStateMachine, self).__init__(
            element_name, element_shape, element_style)


class UMLPackage(UMLOneElement):

    def __init__(self, element_name: str, element_shape="tab", element_style="solid"):
        super(UMLPackage, self).__init__(
            element_name, element_shape, element_style)


class UMLNote(UMLOneElement):

    def __init__(self, element_name: str, element_shape="note", element_style="solid"):
        super(UMLNote, self).__init__(
            element_name, element_shape, element_style)
