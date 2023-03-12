#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - check if a reversed_list is same as unreversed
 * @head: pointer to the head of the linked list
 * Return: 0 if it is not a linked list and vice versa
 */

int is_palindrome(listint_t **head)
{
listint_t *list1 = *head;
listint_t *list2 = *head;
int total = 1, j = 0;
if (list1 == NULL || list2->next == NULL)
return (1);

while (list1->next != NULL)
{
total++;
list1 = list1->next;
}
list1 = *head;
total = (int) total / 2;
while (total > 0)
{
list2 = *head;
while (list2->next != NULL && list2->next->next != NULL)
{
list2 = list2->next;
}
if (list1->n == list2->next->n)
{
j = 1;
}
else
{
return (0);
}
printf("%d == %d\n", list2->next->n, list1->n);
list1 = list1->next;
list2->next = NULL;
total--;
}
return (j);
}
