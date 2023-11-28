#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * list_print - prints all elements of a listint_t list
 * @h: pointer to h of list
 * Return: number of nodes
 */
size_t list_print(const listint_t *h)
{
const listint_t *curr;
unsigned int m; /* number of nodes */
curr = h;
m = 0;
while (curr != NULL)
{
printf("%i\n", curr->n);
curr = curr->nxt;
m++;
}

return (m);
}

/**
 * node_add_end - adds a other node at the end of a listint_t list
 * @h: pointer to pointer of first node of listint_t list
 * @n: integer to be included in other node
 * Return: address of the other element or NULL if it fails
 */
listint_t *node_add_end(listint_t **h, const int n)
{
listint_t *other;
listint_t *curr;

curr = *h;

other = malloc(sizeof(listint_t));
if (other == NULL)
return (NULL);

other->n = n;
other->nxt = NULL;

if (*h == NULL)
*h = other;
else
{
while (curr->nxt != NULL)
curr = curr->nxt;
curr->nxt = other;
}

return (other);
}

/**
 * list_free - frees a list
 * @h: pointer to list to be freed
 * Return: void
 */
void list_free(listint_t *h)
{
listint_t *curr;
while (h != NULL)
{
curr = h;
h = h->nxt;
free(curr);
}
}