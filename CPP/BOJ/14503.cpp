#include <iostream>
#include <vector>

using namespace std;

int N, M;
int dr[4] = { -1, 0, 1, 0 };
int dc[4] = { 0, 1, 0, -1 };
vector<vector<int>> map;
vector<vector<bool>> clean_map;

class Robot {
private:
	int r;
	int c;
	int d;

	bool check(int r, int c) {
		if (0 > r || r >= N) return false;
		if (0 > c || c >= M) return false;
		if (map[r][c]) return false;
		return true;
	};

public:
	Robot(int row, int col, int dir) {
		r = row;
		c = col;
		d = dir;
	}

	bool scan_env() {
		for (int i = 1; i <= 4; i++) {
			int new_d = (d - i + 4) % 4;
			int new_r = r + dr[new_d];
			int new_c = c + dc[new_d];
			if (check(new_r, new_c) && !clean_map[new_r][new_c]) {
				r = new_r;
				c = new_c;
				d = new_d;
				clean_map[r][c] = true;
				return true;
			}
		}
		return false;
	}

	bool conflict() {
		int back_d = (d + 2) % 4;
		int back_r = r + dr[back_d];
		int back_c = c + dc[back_d];
		if (check(back_r, back_c)) {
			r = back_r;
			c = back_c;
			return true;
		}
		else {
			return false;
		}
	}
};

int main() {
	cin >> N >> M;

	int r, c, d;
	cin >> r >> c >> d;
	
  Robot robot(r, c, d);
	
  map.resize(N, vector<int>(M));
	clean_map.resize(N, vector<bool>(M));
	
  for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
			clean_map[i][j] = false;
		}
	}

  clean_map[r][c] = true;
  bool stop = false;
  while (!stop) {
		if (!robot.scan_env() && !robot.conflict()) {
			stop = true;
		}
	}

	int cnt = 0;
	for (vector<bool> row : clean_map) {
		for (bool x : row) {
			if (x) cnt++;
		}
	}
	cout << cnt;
	return 0;
}