#include "Python.h"
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
	Py_ssize_t list_size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyObject *item;
	
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", allocated);
	
	for (Py_ssize_t i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: ", i);
		if (PyBytes_Check(item))
		{
			printf("bytes\n");
			print_python_bytes(item);
		}
		else if (PyFloat_Check(item))
		{
			printf("float\n");
			print_python_float(item);
		}
		else
		{
			printf("unknown\n");
		}
	}
}

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_GET_SIZE(p);
	char *str = PyBytes_AsString(p);
	
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", (size > 10) ? 10 : size);
	
	for (Py_ssize_t i = 0; i < ((size > 10) ? 10 : size); i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < ((size > 10) ? 9 : size - 1))
			printf(" ");
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	double value = PyFloat_AsDouble(p);
	
	printf("  value: %f\n", value);
}
