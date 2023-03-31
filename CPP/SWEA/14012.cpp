#include <iostream>

/* //deprecated;
using namespace std;
int charger[50] = {};
int N, T;
int result;

int dfs(int idx, int charge) {
	if (idx >= N-1)
		return charge;
	for (int i = charger[idx]; i > 0 ; i--) {
		if (charge <= result) {
			int tmp = dfs(idx + i, charge + 1);
			result = (tmp < result) ? tmp : result;
		}
	}
	return result;
}

int main(void) {
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N;
		for (int i = 0; i < N - 1; i++)
			cin >> charger[i];
		result = 50;
		cout << "#" << tc << " " << dfs(0, -1) << endl;
	}
	return 0;
}
*/

#include <iostream>

using namespace std;
int N, T;
int stop[50];
int result;
bool flag;

void solve(int idx, int cnt) {
	if (flag) return;
	if (idx <= 0) {
		result = cnt;
		flag = true;
		return;
	}
	for (int i = 0; i < idx; i++) {
		if (stop[i] + i >= idx) {
			solve(i, cnt + 1);
		}
	}
	return;
}

int main(void) {
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N;
		for (int i = 0; i < N-1; i++)
			cin >> stop[i];
		result = 50;
		flag = false;
		solve(N - 1, -1);
		cout << "#" << tc << " " << result << endl;
	}
	return 0;
}