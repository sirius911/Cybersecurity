#include <string.h>
#include <stdio.h>

int main(void)
{
    char input [100] = {0};
    char code[] = "__stack_check\0";

    printf("Please enter key: ");
    scanf("%s",input);
    if (strcmp(input,code) == 0)
        printf("Good job.\n");
    else
        printf("Nope.\n");
    return 0;
}