#include "lists.h"

/**
 * is_palindrome -checks if a singly linked list is a palindrome.
 * @head: linked list.
 *
 * Return: 0 if it is not a palindrome, otherwise 1.
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j;
	listint_t *ptr = *head;
	int list[2000];

	if (!head || !*head)
		return (1);
	while (ptr)
	{
		list[i++] = ptr->n;
		ptr = ptr->next;
	}
	for (j = 0; j < i / 2; j++)
	{
		if (list[j] != list[i - j - 1])
			return (0);
	}
	return (1);
}
