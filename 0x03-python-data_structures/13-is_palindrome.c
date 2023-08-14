#include "lists.h"

/**
 *  * add_nodeint - adds a new node at the beginning of a listint_t list.
 *   * @head: pointer to listint_t.
 *    * @n: number to add.
 *     *
 *      * Return: pointer to new element.
 *       */
listint_t *add_nodeint(listint_t **head, const int n)
{
		listint_t *new;

		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = n;
		new->next = *head;
		*head = new;
		return (new);
}

/**
 * is_palindrome -checks if a singly linked list is a palindrome.
 * @head: linked list.
 *
 * Return: 0 if it is not a palindrome, otherwise 1.
 */
int is_palindrome(listint_t **head)
{
	int i, j;
	listint_t *ptr = *head, *reverse, *free;

	if (!head || !*head)
		return (1);
	add_nodeint(&reverse, ptr->n);
	reverse->next = NULL;
	for (i = 1; ptr->next; i++)
	{
		add_nodeint(&reverse, ptr->next->n);
		ptr = ptr->next;
	}
	if (i % 2)
	{
		free_listint(reverse);
		return (0);
	}
	ptr = *head;
	free = reverse;
	for (j = 0; j < i / 2; j++)
	{
		if (ptr->n != reverse->n)
		{
			free_listint(free);
			return (0);
		}
		ptr = ptr->next;
		reverse = reverse->next;
	}
	free_listint(free);
	return (1);
}
