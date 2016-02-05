# coding=utf-8
'''
Created on Feb 4, 2016

@author: yangjie
'''
import os
import unittest2

from uml_graphviz.uml_blocks import typeOne
from uml_graphviz.uml_blocks.figure import UMLFigure_Usual


BASE_PATH = ASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
TEM_PATH = BASE_PATH + "/../tem/"


class MainTest(unittest2.TestCase):

    def setUp(self):
        self.figure = UMLFigure_Usual()

    def tearDown(self):
        pass

    def draw(self, name_str):
        name_str += ".eps"
        self.figure.draw_uml(TEM_PATH + name_str)

    def test_class(self):
        self.element = typeOne.UMLClass(
            "Class", ["Attributes", ], ["Operations", ])
        self.figure.add_uml_element(self.element)
        self.draw("FIG_Class")

    def test_interface(self):
        self.element = typeOne.UMLInterface(
            "Interface", ["Attributes", ])
        self.figure.add_uml_element(self.element)
        self.draw("FIG_Interface")

    def test_collaboration(self):
        self.element = typeOne.UMLCollaboration("Collaboration")
        self.figure.add_uml_element(self.element)
        self.draw("FIG_Collaboration")

    def test_use_case(self):
        self.element = typeOne.UMLUseCase("Use Case")
        self.figure.add_uml_element(self.element)
        self.draw("FIG_Use_Case")

    def test_node(self):
        self.element = typeOne.UMLNode("Node")
        self.figure.add_uml_element(self.element)
        self.draw("FIG_Node")

    def test_state_machine(self):
        self.element = typeOne.UMLStateMachine("State Machine")
        self.figure.add_uml_element(self.element)
        self.draw("FIG_State_Machine")

    def test_package(self):
        self.element = typeOne.UMLPackage("Package")
        self.figure.add_uml_element(self.element)
        self.draw("FIG_Package")

    def test_note(self):
        self.element = typeOne.UMLNote("Note")
        self.figure.add_uml_element(self.element)
        self.draw("FIG_Note")

if __name__ == "__main__":
    unittest2.main()
