#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_string - this print python strings 
 * @p: string to be printd
 *
 *
 */

void print_python_string(PyObject *p)
{
PyUnicodeObject *str;
wchar_t *wide_str;
Py_ssize_t length;

if (!PyUnicode_Check(p))
{
printf("Invalid String Object\n");
return (0);
}

str = (PyUnicodeObject *)p;
length = PyUnicode_GetLength(p);
wide_str = PyUnicode_AsWideCharString(p, NULL);

printf("  %ls\n", wide_str);

PyMem_Free(wide_str);
}
