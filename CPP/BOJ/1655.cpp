#include<iostream>
#include<queue>
using namespace std;

priority_queue<int, vector<int>, greater<int>> mnq;
priority_queue<int> mxq;

int mid_heap(int x) {
	mxq.push(x);
	while (mxq.size() != (mxq.size() + mnq.size() + 1) / 2) {
		mnq.push(mxq.top());
		mxq.pop();
	}
	if (mnq.empty()) return mxq.top();
	while (mxq.top() > mnq.top()) {
		mnq.push(mxq.top());
		mxq.push(mnq.top());
		mxq.pop();
		mnq.pop();
	}
	return mxq.top();
}

int main() {
	ios::sync_with_stdio(NULL);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int N;
	cin >> N;
	while (N--) {
		int inp;
		cin >> inp;
		cout << mid_heap(inp) << "\n";
	}
}