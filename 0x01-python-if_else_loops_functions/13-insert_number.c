#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * insert_node - Function inserts a number into a sorted singly linked list.
 * @head: Pointer to the Adress of Head node
 * @number: Value to be inserted in new node
 *
 * Return: Pointer to the New List
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *first;
	int temp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = *head;
	*head = new;

	first  = *head;
	while (first->next)
	{
		if (first->n > first->next->n)
		{
			temp = first->n;
			first->n = first->next->n;
			first->next->n = temp;
		}
		first = first->next;
	}

	return (new);
}
