#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void merge_two(int* a, int na, int* b, int nb, int* result) {
    int i = 0, j = 0, k = 0;
    while (i < na && j < nb) {
        if (a[i] <= b[j]) result[k++] = a[i++];
        else              result[k++] = b[j++];
    }
    while (i < na) result[k++] = a[i++];
    while (j < nb) result[k++] = b[j++];
}

void merge_tree(int** runs, int* sizes, int n_runs, int* output) {
    if (n_runs == 1) {
        for (int i = 0; i < sizes[0]; i++)
            output[i] = runs[0][i];
        return;
    }

    printf("   Processando %d runs...\n", n_runs);

    int* temp = (int*)malloc((sizes[0] + sizes[1]) * sizeof(int));
    if (temp == NULL) {
        printf("Erro: Sem memória!\n");
        exit(1);
    }

    merge_two(runs[0], sizes[0], runs[1], sizes[1], temp);

    free(runs[0]);
    runs[0] = temp;
    sizes[0] = sizes[0] + sizes[1];

    for (int i = 2; i < n_runs; i++) {
        runs[i-1] = runs[i];
        sizes[i-1] = sizes[i];
    }

    merge_tree(runs, sizes, n_runs - 1, output);
}

int main() {
    printf("=== K-WAY MERGE PARALELO (Merge Tree) ===\n");
    printf("Threads disponiveis: %d\n\n", omp_get_max_threads());

    int n_runs = 8;
    int** runs = (int**)malloc(n_runs * sizeof(int*));
    int* sizes = (int*)malloc(n_runs * sizeof(int));

    long total_elements = 0;

    for (int i = 0; i < n_runs; i++) {
        sizes[i] = 10000;
        runs[i] = (int*)malloc(sizes[i] * sizeof(int));
        if (runs[i] == NULL) {
            printf("Erro de alocacao!\n");
            return 1;
        }
        for (int j = 0; j < sizes[i]; j++) {
            runs[i][j] = j * 10 + i;
        }
        total_elements += sizes[i];
    }

    int* result = (int*)malloc(total_elements * sizeof(int));

    double start = omp_get_wtime();

    #pragma omp parallel
    #pragma omp single
    {
        printf("Iniciando Merge Tree com %d runs...\n", n_runs);
        merge_tree(runs, sizes, n_runs, result);
    }

    double end = omp_get_wtime();

    printf("\nMerge concluido com sucesso!\n");
    printf("Tempo de execucao: %.4f segundos\n", end - start);
    printf("Total de elementos: %ld\n", total_elements);

    for (int i = 0; i < n_runs; i++) free(runs[i]);
    free(runs);
    free(sizes);
    free(result);

    return 0;
}