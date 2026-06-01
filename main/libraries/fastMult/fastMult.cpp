#include "fastMult.hpp"

unsigned long long modpow(unsigned long long* base,
                          unsigned long long power,
                          unsigned long long* mod) {

    unsigned long long result = 1;
    unsigned long long b = *base % *mod;  // local copy for speed

    while (power > 0) {

        if (power & 1) {  // if odd
            result = (result * b) % *mod;
        }

        b = (b * b) % *mod;  // square the base
        power >>= 1;         // divide exponent by 2
    }

    return result;
}