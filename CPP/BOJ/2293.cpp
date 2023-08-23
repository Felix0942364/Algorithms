#include <iostream>
#include <vector>

using namespace std;
int cnt[10001] = {0};
int main() {
	int n, k;
	cin >> n >> k;
	cnt[0] = 1;
	vector<int> coins(n);
	for (int i = 0; i < n; i++) cin >> coins[i];
	for (int coin : coins) {
		for (int idx = 1; idx <= k; idx++) {
			if (idx - coin < 0) continue;
			cnt[idx] += cnt[idx - coin];
		}
	}
	cout << cnt[k];
}