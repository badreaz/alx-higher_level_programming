#include "lists.h"

/**
 * is_palindrome -checks if a singly linked list is a palindrome.
 * @head: linked list.
 *
 * Return: 0 if it is not a palindrome, otherwise 1.
 */
int is_palindrome(listint_t **head)
{
	int i;
	listint_t *ptr = *head, *reverse = *head;
	listint_t *prev, *next;

	prev = next = NULL;
	if (!head || !*head)
		return (1);
	while (reverse)
	{
		next = reverse->next;
		reverse->next = prev;
		prev = reverse;
		reverse = next;
	}
	for (i = 0; ptr->next; i++)
	{
		if (ptr->n != reverse->n)
			return (0);
		ptr = ptr->next;
		reverse = reverse->next;
	}
	return (1);
}
