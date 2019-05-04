#include<stdio.h>
#include<stdlib.h>
#include <string.h>
#include "lists.h"
/**
 *print_dlistint - print list
 *@h: list
 *Return: number elements.
 */
size_t print_dlistint(const dlistint_t *h)
{
	int i = 0;

	if (h == NULL)
	{
		return (0);
	}
	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		i++;
	}
	return (i);
}
