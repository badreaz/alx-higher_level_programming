#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints some basic info about python lists.
 * @p: python object.
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *list;

	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
}
