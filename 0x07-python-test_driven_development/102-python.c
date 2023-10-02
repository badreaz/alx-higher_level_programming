#include <stdio.h>
#include "Python.h"

/**
 * print_python_string - prints python string information
 * @p: string object.
 */
void print_python_string(PyObject *p)
{
	PyObject *encoding;

	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		encoding = PyObject_GetAttrString(p, "encoding");
		if (encoding && PyUnicode_Check(encoding))
			printf("  type: %s\n", PyUnicode_AsUTF8(encoding));
		printf("  length: %zd\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
