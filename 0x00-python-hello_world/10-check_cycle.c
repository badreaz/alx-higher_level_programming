#include "lists.h"

/**
 * check_cycle - check if a singly linked listhas a cycle.
 * @list: linked list.
 *
 * Return: 0 if there is no cycle, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	const listint_t *turtle, *rabbit;

	if (!list)
		return (0);

	turtle = rabbit = list;
	while (rabbit)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
		if (turtle == rabbit)
			return (1);
	}
	return (0);
}
