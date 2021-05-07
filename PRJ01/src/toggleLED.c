#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define GPIO_LED "17"
#define GPIO_BUTTON "27"
#define GPIO_LED_PATH "/sys/class/gpio/gpio17/"
#define GPIO_BUTTON_PATH "/sys/class/gpio/gpio27/"
#define GPIO_SYSFS "/sys/class/gpio/"

void writeGPIO(char filename[], char value[])
{
    FILE *file_pointer;
    file_pointer = fopen(filename, "w+");
    fprintf(file_pointer, "%s", value);
    fclose(file_pointer);
}

int main(int argc, char *argv[])
{
    printf("\nStarting the toggleLED program\n");
    printf("----------------------------\n\n");
    usleep(1000000);

    printf("Setting up the LED on the GPIO\n");
    writeGPIO(GPIO_SYSFS "export", GPIO_LED);
    usleep(100000);
    writeGPIO(GPIO_LED_PATH "direction", "out");

    usleep(1000000);

    printf("Setting up the BUTTON on the GPIO\n\n");
    writeGPIO(GPIO_SYSFS "export", GPIO_BUTTON);
    usleep(100000);
    writeGPIO(GPIO_BUTTON_PATH "direction", "in");

    int counter = 0;

    while (counter < 100)
    {
        usleep(100000);

        FILE *file_pointer;
        char line[80], full_file_name[100];
        sprintf(full_file_name, GPIO_BUTTON_PATH "/value");
        file_pointer = fopen(full_file_name, "r");
        
        while (fgets(line, 80, file_pointer) != NULL)
        {
            printf("The state of the BUTTON is %s", line);
        }

        if (line[0] == '1')
        {
            writeGPIO(GPIO_LED_PATH "value", "1");
        }
        else 
        {
            writeGPIO(GPIO_LED_PATH "value", "0");
        }
        fclose(file_pointer);
        counter++;
    }

    usleep(1000000);
    printf("\nTurning the LED off\n");
    writeGPIO(GPIO_LED_PATH "value", "0");

    usleep(1000000);
    printf("Closing the LED on the GPIO\n");
    writeGPIO(GPIO_SYSFS "unexport", GPIO_LED);

    usleep(1000000);
    printf("Closing the BUTTON on the GPIO\n");
    writeGPIO(GPIO_SYSFS "unexport", GPIO_BUTTON);
    
    printf("\n----------------------------\n");
    printf("Finished the toggleLED Program\n\n");
    exit(EXIT_SUCCESS);
}