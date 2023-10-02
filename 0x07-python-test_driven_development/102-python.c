#include <stdio.h>

/**
 * print_python_string - prints python string information
 * @p: string object.
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (PyUnicode_check(p))
	{
		printf("  type: %s\n", PyUnicode_GET_ENCODING(p));
		printf("  length: %zd\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
