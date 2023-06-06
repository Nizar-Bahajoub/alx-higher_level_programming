#include "lists.h"

/**
 * check_cycle - check if ther is a cycle in a list
 * @list: the list to be checked
 *
 * Return: 1if ther is a cycle 0 if not
 */

int check_cycle(listint_t *list)
{
	const listint_t *current, *previous;

	current = list;
	previous = list;

	while (current && previous && list)
	{
		previous = previous->next;
		current = current->next->next;
		if (current == previous)
			return (1);
	}
	return (0);
}
