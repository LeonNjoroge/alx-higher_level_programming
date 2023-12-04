#include <Python.h>

/**
 * print_python_list_info - Outputs info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size;
    int alloc, m;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);

	printf("[*] Allocated = %d\n", alloc);
    m = 0;
	while ( m < size)
	{
		printf("Element %d: ", m);

		obj = PyList_GetItem(p, m);
		printf("%s\n", Py_TYPE(obj)->tp_name);
        m++;
	}
}