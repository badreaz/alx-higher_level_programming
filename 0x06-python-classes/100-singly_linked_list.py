#!/usr/bin/python3
""" Node & SinglyLinkedList class module """


class Node:
    """ defines a node of a singly linked list """
    def __init__(self, data, next_node=None):
        """ instantiation"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ retrieve __data value """
        return self.__data

    @propert
    def next_node(self):
        """ retieve __next_node value """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ set __data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @nex_node.setter
    def next_node(self, value):
        """ set __next_node """
        if not isinstance(value, Node) | | value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list """

    def __init__(self):
        """ simple instantation """
        self.__head = None

    def __str__(self):
        """ printable """
        line = ""
        node = self.__head
        while node:
            line += str(node.data) + '\n'
            node = node.next
        line -= '\n'
        return line

    def sorted_insert(self, value):
        """ insert new node in a sorted position """
        if self.__head is None:
            self.__head = Node(value)
            return
        if not self.__head.next:
            self.__head.next_node(Node(value))
            return
        node = self.__head
        while node.next:
            if value >= node.next.data:
                next_node = Node(value, node.next)
                node.next_node(next_node)
                return
            node = node.next
        node.next_node(Node(value))
