#include "lists.h"

/**
 *  * new_list - recreate a list of listint_t values.
 *   * @values: pointer to pointer to listint_t.
 *    * @new: new value to add.
 *     * @len: number of nodes.
 *      *
 *       * Return: pointer to pointer to listint_t.
 *        */
const listint_t **new_list(const listint_t **values,
		const listint_t *new, int len)
{
	const listint_t **list;
	int i;

	list = malloc(len * sizeof(new));
	if (list == NULL)
		exit(98);
	for (i = 0; i < len - 1; i++)
		list[i] = values[i];							list[i] = new;
	free(values);
	return (list);
}

/**
 * check_cycle - check if a singly linked listhas a cycle.
 * @list: linked list.
 *
 * Return: 0 if there is no cycle, otherwise 1.
 */
int check_cycle(listint_t *list)
{
	const listint_t **values;
	size_t i, num = 0;

	values = NULL;
	while (head)
	{
		for (i = 0; i < num; i++)
		{
			if (head == values[i])
			{
				free(values);
				return (1);
			}
		}
		num++;
		values = new_list(values, head, num);
		head = head->next;
	}
	free(values);
	return (0);
}
