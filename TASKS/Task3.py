#include <stdio.h>
#include <string.h>

#define MAX_TASKS 100
#define MAX_LEN 100

int main() {
    char tasks[MAX_TASKS][MAX_LEN];
    int task_count = 0;
    int choice;

    while(1) {
        printf("\n1.Add 2.View 3.Update 4.Delete 5.Exit\n");
        printf("Choose option: ");
        scanf("%d", &choice);
        getchar(); // to consume the newline

        if(choice == 1) {
            if(task_count < MAX_TASKS) {
                printf("Enter task: ");
                fgets(tasks[task_count], MAX_LEN, stdin);
                tasks[task_count][strcspn(tasks[task_count], "\n")] = '\0'; // remove newline
                task_count++;
                printf("Task Added\n");
            } else {
                printf("Task list full!\n");
            }
        }
        else if(choice == 2) {
            printf("\nYour Tasks:\n");
            for(int i = 0; i < task_count; i++) {
                printf("%d. %s\n", i, tasks[i]);
            }
        }
        else if(choice == 3) {
            int index;
            printf("Enter index to update: ");
            scanf("%d", &index);
            getchar(); // consume newline
            if(index >= 0 && index < task_count) {
                printf("Enter new task: ");
                fgets(tasks[index], MAX_LEN, stdin);
                tasks[index][strcspn(tasks[index], "\n")] = '\0';
                printf("Task Updated\n");
            } else {
                printf("Invalid index!\n");
            }
        }
        else if(choice == 4) {
            int index;
            printf("Enter index to delete: ");
            scanf("%d", &index);
            getchar(); // consume newline
            if(index >= 0 && index < task_count) {
                for(int i = index; i < task_count - 1; i++) {
                    strcpy(tasks[i], tasks[i + 1]);
                }
                task_count--;
                printf("Task Deleted\n");
            } else {
                printf("Invalid index!\n");
            }
        }
        else if(choice == 5) {
            printf("Exiting...\n");
            break;
        }
        else {
            printf("Invalid choice!\n");
        }
    }

    return 0;
}
