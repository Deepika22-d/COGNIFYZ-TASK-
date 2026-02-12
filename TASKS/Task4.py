#include <stdio.h>

int main() {
    int choice;
    float temp, result;

    printf("Temperature Converter\n");
    printf("1. Celsius to Fahrenheit\n");
    printf("2. Fahrenheit to Celsius\n");
    printf("Enter choice (1 or 2): ");
    scanf("%d", &choice);

    printf("Enter temperature: ");
    scanf("%f", &temp);

    if(choice == 1) {
        result = (temp * 9 / 5) + 32;
        printf("%.2f°C = %.2f°F\n", temp, result);
    }
    else if(choice == 2) {
        result = (temp - 32) * 5 / 9;
        printf("%.2f°F = %.2f°C\n", temp, result);
    }
    else {
        printf("Invalid choice! Enter 1 or 2.\n");
    }

    return 0;
}
