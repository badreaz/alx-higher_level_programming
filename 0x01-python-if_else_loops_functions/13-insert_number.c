#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list.
 * @head: linke list.
 * @number: number to insert.
 *
 * Return: adree to new node, or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!list || list->n >= number)
	{
		new->next = list;
		*head = new;
	}
	else
	{
		while (list->next && list->next->n < number)
			list = list->next;
		new->next = list->next;
		list->next = new;
	}
	return (new);
}
