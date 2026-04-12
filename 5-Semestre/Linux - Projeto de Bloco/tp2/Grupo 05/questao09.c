#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 10000

int main() {
    int i, j;
    int brilho = 50;

    int **matriz = (int**) malloc(N * sizeof(int*));
    for (i = 0; i < N; i++) {
        matriz[i] = (int*) malloc(N * sizeof(int));
    }

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            matriz[i][j] = rand() % 256;
        }
    }

    double inicio = omp_get_wtime();

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            matriz[i][j] += brilho;
        }
    }

    double fim = omp_get_wtime();
    printf("Tempo sequencial: %f segundos\n", fim - inicio);
    inicio = omp_get_wtime();

    #pragma omp parallel for shared(matriz) private(i, j)
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            matriz[i][j] += brilho;
        }
    }

    fim = omp_get_wtime();
    printf("Tempo paralelo: %f segundos\n", fim - inicio);

    return 0;
}