#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#include <time.h>

#define MAX_POINTS 100000
#define SPACE_SIZE 1000.0
#define CAPACITY 50
#define MAX_DEPTH 12

typedef struct Point {
    double x, y;
    int id;
} Point;

typedef struct Rectangle {
    double x_min, x_max, y_min, y_max;
} Rectangle;

typedef struct QuadTree {
    Rectangle boundary;
    Point *points;
    int point_count;
    int capacity;
    int divided;
    struct QuadTree *NW, *NE, *SW, *SE;
} QuadTree;

QuadTree* createQuadTree(Rectangle boundary, int capacity) {
    QuadTree* qt = (QuadTree*)malloc(sizeof(QuadTree));
    qt->boundary = boundary;
    qt->capacity = capacity;
    qt->points = (Point*)malloc(capacity * sizeof(Point));
    qt->point_count = 0;
    qt->divided = 0;
    qt->NW = qt->NE = qt->SW = qt->SE = NULL;
    return qt;
}

int contains(Rectangle r, Point p) {
    return (p.x >= r.x_min && p.x < r.x_max && 
            p.y >= r.y_min && p.y < r.y_max);
}

int intersectsCircle(Rectangle r, Point center, double radius) {
    double closestX = fmax(r.x_min, fmin(center.x, r.x_max));
    double closestY = fmax(r.y_min, fmin(center.y, r.y_max));
    double dx = center.x - closestX;
    double dy = center.y - closestY;
    return (dx*dx + dy*dy) <= radius * radius;
}

void subdivide(QuadTree* qt) {
    double x_mid = (qt->boundary.x_min + qt->boundary.x_max) / 2;
    double y_mid = (qt->boundary.y_min + qt->boundary.y_max) / 2;

    Rectangle nw = {qt->boundary.x_min, x_mid, y_mid, qt->boundary.y_max};
    Rectangle ne = {x_mid, qt->boundary.x_max, y_mid, qt->boundary.y_max};
    Rectangle sw = {qt->boundary.x_min, x_mid, qt->boundary.y_min, y_mid};
    Rectangle se = {x_mid, qt->boundary.x_max, qt->boundary.y_min, y_mid};

    qt->NW = createQuadTree(nw, qt->capacity);
    qt->NE = createQuadTree(ne, qt->capacity);
    qt->SW = createQuadTree(sw, qt->capacity);
    qt->SE = createQuadTree(se, qt->capacity);
    qt->divided = 1;
}

int insert(QuadTree* qt, Point p) {
    if (!contains(qt->boundary, p)) return 0;

    if (qt->point_count < qt->capacity && !qt->divided) {
        qt->points[qt->point_count++] = p;
        return 1;
    }

    if (!qt->divided) subdivide(qt);

    if (insert(qt->NW, p)) return 1;
    if (insert(qt->NE, p)) return 1;
    if (insert(qt->SW, p)) return 1;
    if (insert(qt->SE, p)) return 1;
    return 0;
}

void buildParallel(QuadTree* qt, Point* points, int n, int depth) {
    if (n == 0) return;

    if (n <= CAPACITY * 4 || depth >= MAX_DEPTH) {
        for (int i = 0; i < n; i++) {
            insert(qt, points[i]);
        }
        return;
    }

    if (!qt->divided) subdivide(qt);

    Point *nw_pts = malloc(n * sizeof(Point));
    Point *ne_pts = malloc(n * sizeof(Point));
    Point *sw_pts = malloc(n * sizeof(Point));
    Point *se_pts = malloc(n * sizeof(Point));

    int nw_c = 0, ne_c = 0, sw_c = 0, se_c = 0;

    for (int i = 0; i < n; i++) {
        Point p = points[i];
        if (contains(qt->NW->boundary, p))      nw_pts[nw_c++] = p;
        else if (contains(qt->NE->boundary, p)) ne_pts[ne_c++] = p;
        else if (contains(qt->SW->boundary, p)) sw_pts[sw_c++] = p;
        else                                    se_pts[se_c++] = p;
    }

    #pragma omp task
    buildParallel(qt->NW, nw_pts, nw_c, depth + 1);

    #pragma omp task
    buildParallel(qt->NE, ne_pts, ne_c, depth + 1);

    #pragma omp task
    buildParallel(qt->SW, sw_pts, sw_c, depth + 1);

    #pragma omp task
    buildParallel(qt->SE, se_pts, se_c, depth + 1);

}

void freeQuadTree(QuadTree* qt) {
    if (qt == NULL) return;
    if (qt->divided) {
        freeQuadTree(qt->NW);
        freeQuadTree(qt->NE);
        freeQuadTree(qt->SW);
        freeQuadTree(qt->SE);
    }
    free(qt->points);
    free(qt);
}

void query(QuadTree* qt, Point center, double radius, Point* found, int* found_count) {
    if (!intersectsCircle(qt->boundary, center, radius)) return;

    for (int i = 0; i < qt->point_count; i++) {
        double dx = qt->points[i].x - center.x;
        double dy = qt->points[i].y - center.y;
        if (dx*dx + dy*dy <= radius * radius) {
            found[(*found_count)++] = qt->points[i];
        }
    }

    if (qt->divided) {
        query(qt->NW, center, radius, found, found_count);
        query(qt->NE, center, radius, found, found_count);
        query(qt->SW, center, radius, found, found_count);
        query(qt->SE, center, radius, found, found_count);
    }
}

int main() {
    int N = 100000;
    Point* particles = malloc(N * sizeof(Point));

    srand(time(NULL));
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        particles[i].x = (rand() / (double)RAND_MAX) * SPACE_SIZE;
        particles[i].y = (rand() / (double)RAND_MAX) * SPACE_SIZE;
        particles[i].id = i;
    }

    Rectangle boundary = {0, SPACE_SIZE, 0, SPACE_SIZE};
    QuadTree* root = createQuadTree(boundary, CAPACITY);

    printf("Construindo Quadtree paralela...\n");
    double start = omp_get_wtime();

    #pragma omp parallel
    #pragma omp single
    {
        buildParallel(root, particles, N, 0);
    }

    double end = omp_get_wtime();
    printf("Construcao concluida em %.4f segundos\n", end - start);

    Point queryPt = {500.0, 500.0};
    double radius = 50.0;
    Point* found = malloc(N * sizeof(Point));

    printf("Testando consulta...\n");
    int count = 0;
    start = omp_get_wtime();
    query(root, queryPt, radius, found, &count);
    end = omp_get_wtime();

    printf("Encontradas %d particulas em %.4f ms\n", count, (end-start)*1000);

    free(particles);
    free(found);
    freeQuadTree(root);

    printf("Programa executado com sucesso!\n");
    return 0;
}