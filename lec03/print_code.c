builtin_print ( PyObject * self , PyObject * args ,
PyObject * kwds )
{
  static char * kwlist [] = {" sep ", " end ", " file ", 0};
  static PyObject * dummy_args = NULL ;
  static PyObject * unicode_newline = NULL ,
    * unicode_space = NULL ;
  static PyObject * str_newline = NULL ,
    * str_space = NULL ;
  PyObject * newline , * space ;
  PyObject * sep = NULL , * end = NULL , * file = NULL ;
  int i , err , use_unicode = 0 ;
  /*and much more*/
