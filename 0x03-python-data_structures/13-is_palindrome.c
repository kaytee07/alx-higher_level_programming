#include "lists.h"
#include <stdio.h>

/**
 * reverseList - reverse a linked list
 * @head: head of the list about to be reversed
 * Return: head of linked list
 */
/*listint_t *reverseList(listint_t *head)
{
listint_t *prev = NULL;
listint_t *curr = head;
listint_t *next = NULL;
while (curr != NULL)
{
next = curr->next;
curr->next = prev;
prev = curr;
curr = next;
}
return (prev);
}
*/
/**
 * is_palindrome - check if a reversed_list is same as unreversed
 * @head: pointer to the head of the linked list
 * Return: 0 if it is not a linked list and vice versa
 */

int is_palindrome(listint_t **head)
{
listint_t  *slow = *head;
listint_t  *fast = *head;
listint_t  *prev_slow = NULL;
listint_t  *mid_node = NULL;
int is_palindrome = 1;
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}
if (fast != NULL)
{
mid_node = slow;
slow = slow->next;
}
listint_t *second_half = reverseList(slow);
listint_t *first = *head;
listint_t *second = second_half;
while (second != NULL)
{
if (first->n != second->n)
{
is_palindrome = 0;
break;
}
first = first->next;
second = second->next;
}
reverseList(second_half);
if (mid_node != NULL)
{
prev_slow->next = mid_node;
mid_node->next = second_half;
}
else
{
prev_slow->next = second_half;
}
return (is_palindrome);
}
