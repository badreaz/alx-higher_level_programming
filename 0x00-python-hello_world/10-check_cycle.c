#include "lists.h"

/**
 * check_cycle - check if a singly linked listhas a cycle.
 * @list: linked list.
 *
 * Return: 0 if there is no cycle, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rabbit = list;

	if (!list)
		return (0);

	while (rabbit->next->next)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
		if (turtle == rabbit)
			return (1);
	}
	return (0);
}
