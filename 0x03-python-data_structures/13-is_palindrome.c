#include "lists.h"

listint_t *list_rev(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * list_rev - Reverses a singly-linked list.
 * @head: A pointer to the starting node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *list_rev(listint_t **head)
{
	listint_t *nd = *head, *next, *prev = NULL;

	while (nd)
	{
		next = nd->next;
		nd->next = prev;
		prev = nd;
		nd = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 * Return: If is not a palindrome - 0.
 *         If is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temporary, *reverse, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temporary = *head;

	while (temporary)
	{
		size++;
		temporary = temporary->next;
	}

	temporary = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temporary = temporary->next;

	if ((size % 2) == 0 && temporary->n != temporary->next->n)
		return (0);

	temporary = temporary->next->next;
	reverse = list_rev(&temporary);
	mid = reverse;

	temporary = *head;
	while (reverse)
	{
		if (temporary->n != reverse->n)
			return (0);
		temporary = temporary->next;
		reverse = reverse->next;
	}
	list_rev(&mid);

	return (1);
}