#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
/**
 * struct listint_s - singly linked list
 * @m: integer
 * @nxt: points to the nxt node
* singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
int m;
struct listint_s *nxt;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int m);
void list_free(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif 