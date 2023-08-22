#include <iostream>

using namespace std;
// bitmasking
void duplicate(int* check, int sheep) {
    while (sheep) {
        *check |= (1<<(sheep % 10));
        cout << *check << "\n";
        sheep /= 10;
    }
    return;
}

int main(int argc, char** argv)
{
    int test_case;
    int T;
    // bitmasking test set
    int check = (1 << 10) - 1;
    cin >> T;
    for (test_case = 1; test_case <= T; ++test_case)
    {
        int base;
        // bitmasking update set
        int fingerprint = 0;
        int n = 0;
        cin >> base;
        while (check != fingerprint) {
            n++;
            duplicate(&fingerprint, n * base);
        }
        cout << "#" << test_case << " " << n * base << endl;
    }
    return 0;
}