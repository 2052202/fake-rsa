#include <iostream>
#include <numeric> // std::gcd

bool confirm(long long p, long long q, long long e, long long phi_n, long long d) {
    bool ok = true;

    if (p <= 1) {
        std::cout << "Invalid p: p must be a prime greater than 1.\n";
        ok = false;
    }
    if (q <= 1) {
        std::cout << "Invalid q: q must be a prime greater than 1.\n";
        ok = false;
    }
    if (e <= 1) {
        std::cout << "Invalid e: e must be greater than 1.\n";
        ok = false;
    }
    if (e >= phi_n) {
        std::cout << "Invalid e: e must be less than phi(n).\n";
        ok = false;
    }

    if (std::gcd(p, q) != 1) {
        std::cout << "p and q are not coprime: RSA requires gcd(p, q) = 1.\n";
        ok = false;
    }
    if (std::gcd(e, q) != 1) {
        std::cout << "e and q share a factor: gcd(e, q) must be 1 for RSA.\n";
        ok = false;
    }
    if (std::gcd(e, p) != 1) {
        std::cout << "e and p share a factor: gcd(e, p) must be 1 for RSA.\n";
        ok = false;
    }
    if (std::gcd(phi_n, e) != 1) {
        std::cout << "e is not coprime with phi(n): gcd(e, phi(n)) must be 1.\n";
        ok = false;
    }

    if ((e * d) % phi_n != 1) {
        std::cout << "Modular inverse check failed: (e * d) mod phi(n) must equal 1.\n";
        ok = false;
    }

    if (ok) {
        std::cout << "All RSA parameters are valid.\n";
    }

    return ok;
}
