#include <object.h>
#include <unicodeobject.h>
#include <Python.h>


void print_python_string(PyObject *p)
{
const char *kind = NULL;

Py_ssize_t length = 0;

wchar_t *stri = NULL;

printf("[.] string object info\n");
if (!PyUnicode_Check(p))
{
printf("  [ERROR] Invalid String Object\n");
return;
}

if (PyUnicode_IS_COMPACT_ASCII(p))
kind = "compact ascii";
else
kind = "compact unicode object";

stri = PyUnicode_AsWideCharString(p, &length);

printf("  type: %s\n", kind);
printf("  length: %ld\n", length);
printf("  value: %ls\n", stri);
}
