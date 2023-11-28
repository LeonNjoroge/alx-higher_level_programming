#include "lists.h"

listint_t *create_node(int n);

/**
 * insert_node - inserts a node sorted in a linked list
 * @head: double pointer to head for modification in edge
 * cases
 * @number: data for new node
 *
 * Return: pointer to newly created node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node_current = NULL;
listint_t *node_new = NULL;

if (!head)
return (NULL);
else if (!(*head))
{
node_new = create_node(number);
*head = node_new;
return (node_new);
}
node_current = *head;
while (node_current)
{
if (node_current->n >= number)
{
node_new = create_node(number);
node_new->next = node_current;
*head = node_new;
return (node_new);
}
else if (node_current->n <= number)
{
if (!node_current->next || node_current->next->n >= number)
{

node_new = create_node(number);
node_new->next = node_current->next;
node_current->next = node_new;
return (node_current->next);
}
}
node_current = node_current->next;
}
return (NULL); /* failed */
}


/**
 * create_node - creates a new node
 * @n: data to insert
 * Return: pointer to newly allocated node
 */
listint_t *create_node(int n)
{
listint_t *val = NULL;

val = malloc(sizeof(listint_t));
if (!val)
return (NULL);
val->next = NULL;
val->n = n;
return (val);
}