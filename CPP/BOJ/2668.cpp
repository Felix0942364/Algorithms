#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int N;
	cin >> N;
	vector<int> board(N+1);
	vector<int> ans = {};
	vector<int>::iterator iter;
	board[0] = 0;
	for (int i = 1; i <= N; i++) {
		cin >> board[i];
		if (i == board[i]) {
			ans.push_back(i);
			board[i] = 0;
		}
	}

	for (int i = 1; i <= N; i++) {
		int head = board[i];
		int cnt = 0;
		while (head != 0 && head != i && cnt <= N+1) {
			head = board[head];
			cnt++;
		}
		if (head == i || cnt == N+1) {
			while (board[head] != 0) {
				ans.push_back(board[head]);
				int prior = head;
				head = board[head];
				board[prior] = 0;
			}
		}
	}
	sort(ans.begin(), ans.end());
	cout << ans.size() << "\n";
	for (iter = ans.begin(); iter != ans.end(); iter++)
		cout << *iter << "\n";
	return 0;
}