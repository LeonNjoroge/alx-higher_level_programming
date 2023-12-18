#include <bytesobject.h>
#include <object.h>
#include <listobject.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
	long int val;
	int m;
	char *string_try = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &string_try, &val);

	printf("  size: %li\n", val);

	printf("  trying string: %s\n", string_try);
	if (val < 10)
		printf("  first %li bytes:", val + 1);
	else
		printf("  first 10 bytes:");

    m = 0;
	while ( m <= val && m < 10 )
    {
		printf(" %02hhx", string_try[m]);
       m++;
    }
	printf("\n");

}

void print_python_list(PyObject *p)
{
        long int val = PyList_Size(p);

        int m;

        PyListObject *values = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", val);
        printf("[*] Allocated = %li\n", values->allocated);

        m = 0;
        while ( m < val)
        {
            type = (values->ob_item[m])->ob_type->tp_name;
		    printf("Element %i: %s\n", m, type);
            if (!strcmp(type, "bytes"))
                print_python_bytes(values->ob_item[m]);
            m++;
        }
}