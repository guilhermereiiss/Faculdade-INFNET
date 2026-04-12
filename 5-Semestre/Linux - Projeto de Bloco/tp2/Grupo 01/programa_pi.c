#include <stdio.h>
#include <omp.h>

int main() {
    long num_passos = 100000000;
    double passo = 1.0 / (double) num_passos;
    double x, pi, soma = 0.0;

    double inicio = omp_get_wtime();

    #pragma omp parallel for private(x) reduction(+:soma)
    for (long i = 0; i < num_passos; i++) {
        x = (i + 0.5) * passo;
        soma += 4.0 / (1.0 + x * x);
    }

    pi = passo * soma;

    double fim = omp_get_wtime();

    printf("Valor de pi: %f\n", pi);
    printf("Tempo: %f segundos\n", fim - inicio);

    return 0;
}