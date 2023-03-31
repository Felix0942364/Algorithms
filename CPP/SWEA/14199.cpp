#include <iostream>
using namespace std;
 
int price[4];
int days[12];
int tmp[12];
 
int dfs(int i) {
    if (i >= 12) {
        int sum = 0;
        for (int j = 0; j < 12; j++) sum += tmp[j];
        return sum;
    }
    int result = 10000000;
    if (i <= 9) {
        tmp[i] = price[2];
        tmp[i + 1] = 0;
        tmp[i + 2] = 0;
        int tmp_val_1 = dfs(i + 3);
        result = (tmp_val_1 < result) ? tmp_val_1 : result;
    }
    tmp[i] = days[i];
    int tmp_val_2 = dfs(i + 1);
    result = (tmp_val_2 < result) ? tmp_val_2 : result;
    return result;
}
 
int min() {
    for (int i = 0; i < 12; i++) days[i] = (days[i] * price[0] < price[1]) ? days[i] * price[0] : price[1];
    int result = dfs(0);
    if (result < price[3]) return result;
    return price[3];
}
 
int main() {
    int T;
    cin >> T;
    for (int tc = 1; tc < T + 1; tc++) {
        for (int i = 0; i < 4; i++) cin >> price[i];
        for (int i = 0; i < 12; i++) cin >> days[i];
        cout << '#' << tc << " " << min() << endl;
    }
}