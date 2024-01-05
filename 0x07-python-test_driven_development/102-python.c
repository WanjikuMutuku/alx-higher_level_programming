#include <Python.h>

void print_python_string(PyObject *p) {
    Py_ssize_t length;
    Py_UNICODE *value;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    value = PyUnicode_AS_UNICODE(p);

    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        printf("  type: compact ascii\n");
    } else {
        printf("  type: compact unicode object\n");
    }

    printf("  length: %zd\n", length);

    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        printf("  value: %s\n", PyUnicode_AsUTF8(p));
    } else {
        printf("  value: %ls\n", value);
    }
}
