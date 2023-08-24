#include <iostream>
#include <queue>
#define MAX_NODE 501
using namespace std;

int build_time[MAX_NODE];
int build_order[MAX_NODE][MAX_NODE];
int real_time[MAX_NODE];

int main() {
	int N;
	cin >> N;
	queue<int> q;
	int t;
	int inp;
	for (int i = 0; i < MAX_NODE; i++) {
		build_time[i] = -1;
		real_time[i] = -1;
		for (int j = 0; j < MAX_NODE; j++) build_order[i][j] = -1;
	}

	for (int i = 0; i < N; i++) {
		cin >> t;
		build_time[i] = t;
		cin >> inp;
		if (inp < 0) {
			real_time[i] = build_time[i];
			continue;
		}
		for (int j = 0; inp > 0; j++) {
			build_order[i][j] = inp - 1;
			cin >> inp;
		}
		q.push(i);
	}
			
	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		bool flag = true;
		for (int build : build_order[cur]) {
			if (build == -1) break;
			if (real_time[build] == -1) {
				q.push(cur);
				flag = false;
				break;
			}
		}
		if (!flag) continue;
		for (int build : build_order[cur]) {
			if (build == -1) break;
			real_time[cur] = max(real_time[cur], build_time[cur] + real_time[build]);
		}
	}
	for (int i = 0; i < N; i ++)
		cout << real_time[i] << "\n";
	return 0;
}