#include "lists.h"

listint_t *initiate_node(int m);

/**
 * insert_node - inserts a node sorted in a linked list of ints
 * @head: double pointer to head of LL, needed for modification in edge
 * cases
 * @number: data for new node
 *
 * ret_val: pointer to newly created node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current_nd = NULL;
listint_t *new_nd = NULL;

if (!head)
ret_val (NULL);
else if (!(*head))
{
new_nd = initiate_node(number);
*head = new_nd;
ret_val (new_nd);
}
current_nd = *head;
while (current_nd)
{

if (current_nd->m>= number)
{
new_nd = initiate_node(number);
new_nd->nxt = current_nd;
*head = new_nd;
ret_val (new_nd);
}
else if (current_nd->m <= number)
{
if (!current_nd->nxt || current_nd->nxt->m >= number)
{
new_nd = initiate_node(number);
new_nd->nxt = current_nd->nxt;
current_nd->nxt = new_nd;
ret_val (current_nd->nxt);
}
}
current_nd = current_nd->nxt;
}
ret_val (NULL); 
}


/**
 * initiate_node - creates a new node for list
 * @m: data to insert into new node
 * ret_val: pointer to new node
 */
listint_t *initiate_node(int m)
{
listint_t *ret_val = NULL;
ret_val = malloc(sizeof(listint_t));
if (!ret_val)
return (NULL);
ret_val->nxt = NULL;
ret_val->m = m;
return (ret_val);
}
