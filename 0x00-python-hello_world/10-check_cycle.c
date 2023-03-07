#include "lists.h"

/**
 *check_cycle - check if linked list has a cycle
 *@list: linked list to be checked
 *Return: 1 if a cycle is found and 0 if not
 *
 */

int check_cycle(listint_t *list)
{
listint_t *next_node = list;
listint_t *next_two_node = list;

while (next_two_node != NULL && next_two_node->next != NULL)
{
next_node = next_node->next;
next_two_node = next_two_node->next->next;

if (next_node == next_two_node)
return (1);
}
return (0);
}
