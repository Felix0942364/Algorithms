#include <iostream>
#include <queue>
#define MAX_NODE 501
using namespace std;

// base container for algorithm data;
int build_time[MAX_NODE];
int build_order[MAX_NODE][MAX_NODE];
int real_time[MAX_NODE];

int main() {
	int N;
	cin >> N;
	queue<int> q;
	int t;
	int inp;
	// init data container
	for (int i = 0; i < MAX_NODE; i++) {
		build_time[i] = -1;
		real_time[i] = -1;
		for (int j = 0; j < MAX_NODE; j++)
			build_order[i][j] = -1;
	}
	// input data
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
	// pushback node to back order such that prerequisite nodes are processed first
	// max time complexity O(n^2/2)
	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		bool flag = true;
		for (int build : build_order[cur]) {
			if (build == -1) break; // -1 indicator for end
			if (real_time[build] == -1) {
				q.push(cur); // if a prerequisite has not been built pushback
				flag = false;
				break;
			}
		}
		if (!flag) continue;
		for (int build : build_order[cur]) {
			if (build == -1) break;
			// consider the maximum time within the prerequisites as the bottleneck for the process
			// assume that the constant time of the bottlenect + the build time as the end of process
			real_time[cur] = max(real_time[cur], build_time[cur] + real_time[build]);
		}
	}
	// print the processed time as the result
	for (int i = 0; i < N; i ++)
		cout << real_time[i] << "\n";
	return 0;
}