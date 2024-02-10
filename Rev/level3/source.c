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
    test[0] = '*';
    
    printf("Please enter key: ");
    if (scanf("%23s", input) != 1 ) {
        no();
    }

    int i = 1; // Commence à remplir test à partir de l'indice 1
    int index = 2; // Commence la lecture de input à l'indice 2

    while(strlen(test) < 8 && index < strlen(input)) {
        char block[4] = {input[index], input[index + 1], input[index + 2], '\0'}; // Prépare un bloc de trois caractères
        test[i++] = (char)atoi(block); // Convertit le bloc en un nombre, puis en un caractère
        index += 3; // Avance de trois caractères dans input pour le prochain cycle
    }
    test[i] = '\0'; // Assure que decrypt_input est correctement terminé par '\0'

    if (strcmp(test, "********") == 0) {
        ok();
    } else {
        no();
    }

    return 0;
}
