#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        /* Reverse the first half of the list while finding the middle */
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    /* If the linked list has an odd number of elements, skip the middle */
    if (fast != NULL)
        slow = slow->next;

    /* Compare the reversed first half with the second half */
    while (slow != NULL)
    {
        if (prev->n != slow->n)
            return (0);

        prev = prev->next;
        slow = slow->next;
    }

    return (1); /* It's a palindrome */
}
