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
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %zd\n", PyUnicode_GET_SIZE(p));
		printf("  value: %s\n", PyUnicode_AS_UNICODE(p));
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
