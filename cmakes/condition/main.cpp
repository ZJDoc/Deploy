#include <iostream>

int main() {
#ifdef HAHA
    std::cout <<"Hello HAHA"<<std::endl;
#else
    std::cout << "Hello ..." << std::endl;
#endif

#ifdef AHAH
    std::cout << "Hello AHAH" << std::endl;
#endif

    std::cout << "Hello, World!" << std::endl;
    return 0;
}
