#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linekd list
 * @head: the head of the list
 * @number: the content of the node to be added
 *
 * Return: the address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev;
	listint_t *next, *new;

	prev = *head;
	next = prev->next;
	new = malloc(sizeof(listint_t));
	new->n = number;
	if (head == NULL || *head == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	while (prev != NULL)
	{
		if (number >= prev->n)
		{
			if (number <= next->n)
			{
				prev->next = new;
				new->next = next;
				return (*head);
			}
			else
			{
				prev->next =new;
				new->next = NULL;
			}
		}
		else
		{
			*head = new;
			new->next = prev;
			return (*head);
		}
		prev = prev->next;
		next = prev->next;
	}
	return (NULL);
}
