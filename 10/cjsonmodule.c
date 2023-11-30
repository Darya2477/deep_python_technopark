#include <Python.h>
#include <jansson.h>

static PyObject *cjson_loads(PyObject *self, PyObject *args)
{
    const char *json_str;
    if (!PyArg_ParseTuple(args, "s", &json_str))
    {
        return NULL;
    }

    json_error_t error;
    json_t *root = json_loads(json_str, 0, &error);
    if (!root || !json_is_object(root))
    {
        PyErr_Format(PyExc_TypeError, "Expected object or value");
        json_decref(root);
        return NULL;
    }

    PyObject *dict = PyDict_New();
    if (!dict)
    {
        PyErr_SetString(PyExc_MemoryError, "Failed to create dict object");
        return NULL;
    }

    const char *key;
    json_t *value;
    void *iter = json_object_iter(root);
    while (iter)
    {
        key = json_object_iter_key(iter);
        value = json_object_iter_value(iter);
        if (json_is_string(value))
        {
            PyObject *py_value = Py_BuildValue("s", json_string_value(value));
            PyDict_SetItemString(dict, key, py_value);
            Py_DECREF(py_value);
        }
        else if (json_is_integer(value))
        {
            PyObject *py_value = Py_BuildValue("i", (int)json_integer_value(value));
            PyDict_SetItemString(dict, key, py_value);
            Py_DECREF(py_value);
        }

        iter = json_object_iter_next(root, iter);
    }

    json_decref(root);
    return dict;
}

static PyObject *cjson_dumps(PyObject *self, PyObject *args)
{
    PyObject *obj;
    if (!PyArg_ParseTuple(args, "O", &obj))
    {
        return NULL;
    }
    if (!PyDict_Check(obj))
    {
        PyErr_SetString(PyExc_TypeError, "Argument must be a dictionary");
        return NULL;
    }

    json_t *root = PyDict_to_json(obj);
    if (!root)
    {
        PyErr_SetString(PyExc_Exception, "Error creating JSON object from dictionary");
        return NULL;
    }

    char *dumped = json_dumps(root, JSON_ENCODE_ANY);
    PyObject *result = Py_BuildValue("s", dumped);
    json_decref(root);
    free(dumped);
    return result;
}

static PyMethodDef cjson_methods[] = {
    {"loads", cjson_loads, METH_VARARGS, "Parse JSON and return string"},
    {"dumps", cjson_dumps, METH_VARARGS, "Serialize string to JSON"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef cjsonmodule = {
    PyModuleDef_HEAD_INIT,
    "cjson",
    "A module for parsing and serializing JSON",
    -1,
    cjson_methods};

PyMODINIT_FUNC PyInit_cjson(void)
{
    PyObject *m;
    m = PyModule_Create(&cjsonmodule);
    if (m == NULL)
    {
        return NULL;
    }
    return m;
}