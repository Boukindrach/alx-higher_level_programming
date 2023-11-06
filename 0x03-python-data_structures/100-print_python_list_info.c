#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
    int size, i;
    PyObject *obj;

    if (!PyList_Check(p))
    {
        PyErr_SetString(PyExc_TypeError, "p must be a list");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}
