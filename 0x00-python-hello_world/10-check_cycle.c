#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: Parameter
 *
 * Return: 0 if there is no cycle, 1 if otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *checked = list;

	while (current != NULL)
	{
		if (checked != NULL)
			checked->next = NULL;

		while (checked != NULL)
		{
			if (current == checked)
			{
				return (1);
			}
			checked = checked->next;
		}
		checked->next = current;
		current = current->next;
	}
	return (0);
}
