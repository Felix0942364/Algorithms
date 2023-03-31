#include <iostream>
#include <cstring>

int board[4][4];
bool valid[10000000];
int result;
int dr[4] = {-1, 1, 0, 0};
int dc[4] = { 0, 0, -1, 1 };

using namespace std;

int pow(int exponent) {
	int tmp = 1;
	while (exponent--) tmp *= 10;
	return tmp;
}

void dfs(int r, int c, int idx, int memo) {
	if (idx == 7) {
		if (!valid[memo]) {
			result += 1;
			valid[memo] = true;
		}
		return;
	}
	for (int i = 0; i < 4; i++) {
		if (r + dr[i] < 4 && r + dr[i] >= 0) {
			if (c + dc[i] < 4 && c + dc[i] >= 0) {
				dfs(r + dr[i], c + dc[i], idx + 1, memo + board[r + dr[i]][c + dc[i]] * pow(idx));
			}
		}
	}
	return;
}

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> board[i][j];
			}
		}
		result = 0;
		memset(valid, false, sizeof(valid));
		for (int r = 0; r < 4; r++) {
			for (int c = 0; c < 4; c++) {
				dfs(r, c, 0, 0);
			}
		}
		cout << "#" << tc << " " << result << endl;
	}
	return 0;
}