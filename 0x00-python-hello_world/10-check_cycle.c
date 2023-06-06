#include "lists.h"

/**
 * check_cycle - check if ther is a cycle in a list
 * @list: the list to be checked
 *
 * Return: 1if ther is a cycle 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *previous = list;

	if (list == NULL)
		return (0);
	while (current && previous && current->next)
	{
		previous = previous->next;
		current = current->next->next;
		if (current == previous)
			return (1);
	}
	return (0);
}
