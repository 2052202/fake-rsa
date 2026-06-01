#include <iostream>
#include <numeric>
#include "ModularInverse.hpp"

long long MultModInverse(long long a, long long n) {
    long long r0 = n, r1 = a;
    long long t0 = 0, t1 = 1;

    while (r1 != 0) {
        long long q = r0 / r1;

        long long r2 = r0 - q * r1;
        r0 = r1;
        r1 = r2;

        long long t2 = t0 - q * t1;
        t0 = t1;
        t1 = t2;
    }

    // If gcd(a, n) != 1, inverse does not exist
    if (r0 != 1) {
        std::cout << "Error: modular inverse does not exist because gcd(a, n) != 1.\n";
        return -1;
    }

    // Normalize to positive range
    long long inverse = t0 % n;
    if (inverse < 0)
        inverse += n;

    return inverse;
}
