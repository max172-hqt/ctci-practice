/* https://www.geeksforgeeks.org/find-local-minima-array/ */

/* Input: arr[] = {9, 6, 3, 14, 5, 7, 4}; */
/* Output: Index of local minima is 2 */

#include <stdio.h>

int local_minima(int arr[], int n);
int local_minima_util(int arr[], int n, int lo, int hi);

int main(void)
{
    int arr[] = {9, 6, 3, 14, 5, 7, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Local minima is %d\n", local_minima(arr, n));

    return 0;
}

int local_minima(int arr[], int n)
{
    return local_minima_util(arr, n, 0, n-1);
}

int local_minima_util(int arr[], int n, int lo, int hi)
{
    if (n == 0) return -1; 
    if (n == 1) return arr[0];

    int middle;
    while (lo <= hi) {
        middle = lo + (hi - lo) / 2;

        if (middle == lo || middle == hi || arr[middle] < arr[middle+1] && arr[middle] < arr[middle-1]) {
            return middle;
        } else if (arr[middle] > arr[middle-1]) {
            hi = middle - 1;
        } else if (arr[middle] > arr[middle+1]) {
            lo = middle + 1;
        }
    }

    return -1;
}
