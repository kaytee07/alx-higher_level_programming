#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert node in ordered linkedlist
 * @head: sorted linked list
 * @number: number to be inserted in sorted list
 * Return: address of inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node;
listint_t *sorted_list = *head;
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);
new_node->n = number;
new_node->next = NULL;

if (sorted_list == NULL || sorted_list->n >= number)
{
new_node->next = sorted_list;
*head = sorted_list;
return (new_node);
}

while (sorted_list->next != NULL)
{
if (sorted_list && sorted_list->n < number &&
(sorted_list->next->n > number || sorted_list->next == NULL))
{
new_node->next = sorted_list->next;
sorted_list->next = new_node;
break;
}
sorted_list = sorted_list->next;
}
return (sorted_list);
}
