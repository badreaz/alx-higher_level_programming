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
	reverse = prev;
	while (ptr->next && reverse)
	{
		if (ptr->n != reverse->n)
			return (0);
		ptr = ptr->next;
		reverse = reverse->next;
	}
	if (reverse)
		return (0);
	return (1);
}
