#include <stdio.h>
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes.
 * Note: Both ** and *returnSize and *returnColumnSizes must be malloced.
 */

int compare(const void *a, const void *b) {
    int *intervalA = *(int **)a;
    int *intervalB = *(int **)b;
    return intervalA[0] - intervalB[0];
}

int** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes) {
    if (intervalsSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    
    // Sort intervals by start time
    qsort(intervals, intervalsSize, sizeof(int*), compare);
    
    // Allocate memory for result
    int** result = (int**)malloc(intervalsSize * sizeof(int*));
    *returnColumnSizes = (int*)malloc(intervalsSize * sizeof(int));
    
    // Add first interval
    result[0] = (int*)malloc(2 * sizeof(int));
    result[0][0] = intervals[0][0];
    result[0][1] = intervals[0][1];
    (*returnColumnSizes)[0] = 2;
    int resultSize = 1;
    
    // Merge overlapping intervals
    for (int i = 1; i < intervalsSize; i++) {
        int start = intervals[i][0];
        int end = intervals[i][1];
        int lastEnd = result[resultSize - 1][1];
        
        if (start <= lastEnd) {
            // Merge intervals
            result[resultSize - 1][1] = (end > lastEnd) ? end : lastEnd;
        } else {
            // Add new interval
            result[resultSize] = (int*)malloc(2 * sizeof(int));
            result[resultSize][0] = start;
            result[resultSize][1] = end;
            (*returnColumnSizes)[resultSize] = 2;
            resultSize++;
        }
    }
    
    *returnSize = resultSize;
    return result;
}

// Time complexity: O(n log n)
// Space complexity: O(n)