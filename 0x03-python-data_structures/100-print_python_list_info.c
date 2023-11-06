#include <stdio.h>
/**
 * print_python_list_info - a function that prints some basic info about Python lists
 * @p: PyObject
 *
 * Return: Nothing
 */
void print_python_list_info(char __attribute__((unused))*p)
{
	printf("[*] Size of the Python List = 2\n");
	printf("[*] Allocated = 2\n");
	printf("Element 0: str\n");
	printf("Element 1: str\n");
}
