#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;
    // Buggy code: multiplies instead of adds
    std::cout << (a * b) << std::endl;
    return 0;
}
