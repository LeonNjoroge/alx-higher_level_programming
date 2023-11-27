#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has cycle
 * @list: pointer to the list
 * Return: 0 if no cycle,
 * 1 if  cycle present
 */
int check_cycle(listint_t *list)
{
	listint_t *second_pointer;
	listint_t *previous;

	second_pointer = list;
	previous = list;
	for (; list && second_pointer && second_pointer->next;)
	{
		list = list->next;
		second_pointer = second_pointer->next->next;
		if (list == second_pointer)
		{
			list = previous;
			previous =  second_pointer;
			while (1)
			{
				second_pointer = previous;
				for (; second_pointer->next != list && second_pointer->next != previous;)
				{
					second_pointer = second_pointer->next;
				}
				if (second_pointer->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
