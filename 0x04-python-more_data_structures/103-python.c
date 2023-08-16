#include <Python.h>

/**
 * print_python_bytes - print basic info about python list bytes.
 * @p: python object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *list;
	int size = 10, i;

	list = (PyBytesObject *)p;
	printf("[.] bytes object info\n");
       	printf("  size: %zd\n", PyObject_VAR_SIZE(p));
	printf("  trying string: %s", list->ob_sval);
	if ((int)PyObject_VAR_SIZE(p) < 10)
		size = (int)PyObject_VAR_SIZE(p) + 1;
	printf("  first %d bytes:", size);
	for (i = 0; i < size; i++)
	{
		printf(" %02x", list->ob_sval[i]);
	}
	printf("\n");
}

/**
 * print_python_list - print basic info about python lists.
 * @p: python object.
 */
void print_python_list(PyObject *p)
{
	int i;
	PyListObject *list;

	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", list->ob_size);
	printf("[*] Allocated = %d\n", list->allocated);
	for (i = 0; i < list->ob_size; i++)
	{
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check(list->ob_item))
			print_python_bytes(list->ob_item);

	}
}
