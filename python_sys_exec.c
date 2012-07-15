#include <python2.7/Python.h>
int main(int argc, char *argv[])
{
  Py_Initialize();
  PyRun_SimpleString("import sys\nprint repr(sys.executable)\n");
  Py_Finalize();
  return 0;
  }
