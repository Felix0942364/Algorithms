#include <iostream>
#include <vector>

using namespace std;

class BigInt {
private:
    std::vector<int> digits; // Stores the digits of the bigint in reverse order

public:
    BigInt() {}

    BigInt(int num) {
        if (num == 0) {
            digits.push_back(0);
            return;
        }
        while (num > 0) {
            digits.push_back(num % 10);
            num /= 10;
        }
    }

    BigInt operator*(const BigInt& other) const {
        BigInt result;
        result.digits.resize(digits.size() + other.digits.size(), 0);
        for (int i = 0; i < digits.size(); ++i) {
            int carry = 0;
            for (int j = 0; j < other.digits.size() || carry; ++j) {
                long long current = result.digits[i + j] +
                    static_cast<long long>(digits[i]) * (j < other.digits.size() ? other.digits[j] : 0) + carry;
                result.digits[i + j] = static_cast<int>(current % 10);
                carry = static_cast<int>(current / 10);
            }
        }
        while (result.digits.size() > 1 && result.digits.back() == 0) result.digits.pop_back();
        return result;
    }

    friend ostream& operator<<(ostream& os, const BigInt& bigint) {
        for (int i = bigint.digits.size() - 1; i >= 0; --i) os << bigint.digits[i];
        return os;
    }
};


int main() {
    int N;
    cin >> N;
    vector<bool> prime(N + 1, true);
    vector<int> divisor = {};
    for (int i = 2; i <= N; i++) {
        if (!prime[i]) continue;
        int cnt = 0;
        for (int j = i; j <= N; j *= i) {
            cnt += N / j;
            for (int k = j; k <= N; k += j)
                prime[k] = false;
        }
        divisor.push_back(cnt);
    }
    BigInt ans(1);
    for (unsigned long int i = 0; i < divisor.size(); i++) {
        ans = ans * (2 * divisor[i] + 1);
    }
    cout << ans;
    return 0;
}