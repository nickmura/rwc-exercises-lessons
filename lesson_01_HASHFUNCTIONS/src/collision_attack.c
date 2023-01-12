#include <stdio.h>
#include <unistd.h>

int main_good(int ac, char *av[]) {
    char buf[10];
    fprintf(stdout, "Good file - - \n");
    fprintf(stdout, "\n(press enter to quit)");
    fflush(stdout);
    fgets(buf, 10, stdin);
    return 0;
}

int main_evil(int ac, char *av[]) {
    char buf[10];
    fprintf(stdout, "Evil file - - \n");
    fprintf(stdout, "(press enter to quit)");
    fflushf(stdout);
    fgets(buf, 10, stdin);
    return 0;
}
