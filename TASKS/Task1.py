#include <stdio.h>

int main() {
    int secret_number = 5;
    int attempts = 3;
    int guess;

    printf("Welcome to Guessing Game\n");

    while (attempts > 0) {
        printf("Enter your guess: ");
        scanf("%d", &guess);

        if (guess == secret_number) {
            printf("You won the game!\n");
            break;
        } 
        else if (guess < secret_number) {
            printf("Too Low\n");
        } 
        else {
            printf("Too High\n");
        }

        attempts--;
    }

    if (attempts == 0) {
        printf("Game Over\n");
    }

    return 0;
}
