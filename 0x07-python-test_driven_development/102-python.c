#include <stdio.h>
#include "Python.h"

/**
 * print_python_string - prints python string information
 * @p: string object.
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		printf("  type: %s\n", (char *)PyUnicode_GET_ENCODING(p));
		printf("  length: %zd\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %s\n", (char *)PyUnicode_AsUTF8(p));
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
