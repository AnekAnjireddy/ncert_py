#include <stdio.h>
#include<math.h>

long long BinomCoeff(int n, int k) {
    if (k < 0 || k > n) {
	    return 0;
    }
    if (k == 0 || k == n) {
	    return 1;
    }

    long long result = 1;
    k = (k < n - k) ? k : n - k;
    
    for (int i = 0; i < k; i++) {
        result *= (n - i);
        result /= (i + 1);
    }
    
    return result;
}

int main() {
    int n = 5;            
    double p = 0.5;       
    int k = 3;            
    
    long long coeff = BinomCoeff(n, k);
    double probability = coeff * pow(p, k) * pow(1 - p, n - k);

    printf("Probability of getting an odd number exactly 3 times: %.4lf\n", probability);

    return 0;
}

