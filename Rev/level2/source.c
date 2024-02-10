#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void no() {
    printf("No\n");
    exit(1);
}

void ok() {
    printf("Good job.\n");
    exit(0);
}

int main(void) {
    char input[24];
    char test[9] = {0};
    test[0] = 'd';
    
    printf("Please enter key: ");
    if (scanf("%23s", input) != 1 || input[0] != '0' || input[1] != '0') {
        no();
    }

    int i = 2; // Start from index 2 to skip the first two '0' characters
    while (input[i] != '\0') {
        char part[4]; // Store each part of 3 characters from input
        strncpy(part, input + i, 3); // Copy 3 characters from input to part
        part[3] = '\0'; // Null-terminate the string
        test[strlen(test)] = (char)atoi(part); // Convert part to integer and store it in test
        i += 3; // Move to the next part in input
        // printf("test = %s\n", test);
    }

    if (strcmp(test, "delabere") == 0) {
        ok();
    } else {
        no();
    }

    return 0;
}
