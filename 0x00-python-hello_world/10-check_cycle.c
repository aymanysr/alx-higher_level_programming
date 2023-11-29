#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list is cyclic
 * @list: pointer to head of list to check
 * Return: 0 if acyclic, 1 if cyclic
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);
	slow = list;
	fast = list->next;
	while (fast && fast->next)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
