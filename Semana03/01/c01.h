/*Programa 1 
  Guilherme Gonzaga Silva
  11621EMT021
*/

#ifndef complexo_h
#define complexo_h
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

struct complexo
{
    double re;
    double im;
};

void inicializaComplexo(struct complexo *nc)
{
    nc->re = 0;
    nc->im = 0;
}
 
void leiaComplexo(struct complexo *nc)
{
    printf("Digite a parte real do complexo: ");
    scanf("%lf", &nc->re);
    printf("Digite a parte imaginaria do complexo: ");
    scanf("%lf", &nc->im);
}
 
void escrevaComplexo(struct complexo *nc)
{
    printf("%lf+%lfi", nc->re, nc->im);
}

void escrevaPolar(struct complexo *nc)
{
    printf("%lf < %lf graus", nc->re, nc->im);
}
 
struct complexo* somaComplexos(struct complexo *nc, struct complexo *ncA)
 {
    struct complexo *ncR = (struct complexo*)malloc(sizeof(struct complexo));
    ncR->re = nc->re + ncA->re;
    ncR->im = nc->im + ncA->im;
  
    return ncR;
}

struct complexo* subComplexos(struct complexo *nc, struct complexo *ncA)
 {
    struct complexo *ncRs = (struct complexo*)malloc(sizeof(struct complexo));
    ncRs->re = nc->re - ncA->re;
    ncRs->im = nc->im - ncA->im;
  
    return ncRs;
}

struct complexo* divComplexos(struct complexo *nc, struct complexo *ncA)
{
    struct complexo *ncRp = (struct complexo*)malloc(sizeof(struct complexo));
    ncRp->re = ((nc->re * ncA->re)-(nc->im * ncA->im)) / (((ncA->re) * (ncA->re))+((ncA->im) * (ncA->im)));
    ncRp->im = ((nc->re * ncA->im)+(nc->im * ncA->re)) / (((ncA->re) * (ncA->re))+((ncA->im) * (ncA->im)));

    return ncRp;
}

struct complexo* multiComplexos(struct complexo *nc, struct complexo *ncA)
{
    struct complexo *ncRm = (struct complexo*)malloc(sizeof(struct complexo));
    ncRm->re = ((nc->re * ncA->re)-(nc->im * ncA->im));
    ncRm->im = ((nc->re * ncA->im)+(nc->im * ncA->re));

    return ncRm;
}
/*
struct complexo* convComplexos(struct complexo *nc)
{
    struct complexo *ncRc = (struct complexo*)malloc(sizeof(struct complexo));
    double a = nc->re;
    double b = nc->im;
    ncRc->re = sqrt((a*a) + (b*b));
    ncRc->im = atan2(b, a);
    
    return ncRc;
}
*/

#endif