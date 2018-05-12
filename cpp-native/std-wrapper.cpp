#include "Python.h"
#include "std.h"

struct module_state {
    PyObject *error;
};

#if PY_MAJOR_VERSION >= 3
#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))
#else
#define GETSTATE(m) (&_state)
static struct module_state _state;

extern "C" {
    void initstd(void);
}
#endif

static PyObject *error_out(PyObject * m) {
    struct module_state *st = GETSTATE(m);
    PyErr_SetString(st->error, "something bad happened");
    return NULL;
}

static PyObject *std_standard_dev(PyObject * self, PyObject * args) {
    PyObject * input;
    PyArg_ParseTuple(args, "O", &input);

    int size = PyList_Size(input);

    std::vector<double> list;
    list.resize(size);

    for (int i = 0; i < size; i++) {
        list[i] = PyFloat_AS_DOUBLE(PyList_GET_ITEM(input, i));
    }

    return PyFloat_FromDouble(standardDeviation(list));
}

static PyMethodDef std_methods[] = {
        {"error_out",    (PyCFunction) error_out, METH_NOARGS, NULL},
        {"standard_dev", std_standard_dev,        METH_VARARGS, "Return the standard deviation of a list."},
        {NULL, NULL}
};

#if PY_MAJOR_VERSION >= 3

static int std_traverse(PyObject * m, visitproc visit, void *arg) {
Py_VISIT(GETSTATE(m)->error);
return 0;
}

static int std_clear(PyObject * m) {
    Py_CLEAR(GETSTATE(m)->error);
    return 0;
}


static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "std",
        NULL,
        sizeof(struct module_state),
        std_methods,
        NULL,
        std_traverse,
        std_clear,
        NULL
};

#define INITERROR return NULL

PyMODINIT_FUNC PyInit_std(void)

#else
#define INITERROR return

void initstd(void)
#endif
{
#if PY_MAJOR_VERSION >= 3
    PyObject * module = PyModule_Create(&moduledef);

    if (module == NULL)
        INITERROR;
    struct module_state *st = GETSTATE(module);

    st->error = PyErr_NewException("std.Error", NULL, NULL);
    if (st->error == NULL) {
        Py_DECREF(module);
        INITERROR;
    }
#else
    Py_InitModule("std", std_methods);
#endif

#if PY_MAJOR_VERSION >= 3
    return module;
#endif
}
