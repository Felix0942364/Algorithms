#include <iostream>
#include <vector>

using namespace std;
const int MAX_NODE = 5000;

struct Node {
	int data;
	Node* next;

	Node(int data) : data(data), next(nullptr) {}
};

class LinkedList {
private:
	Node* head;
	Node* tail;
	vector<Node*> nodeArr;
	int nodeCnt;

public:
	LinkedList() : head(nullptr), tail(nullptr), nodeCnt(0) {
		nodeArr.resize(MAX_NODE, nullptr);
	}

	Node* getNewNode(int data) {
		nodeArr[nodeCnt] = new Node(data);
		return nodeArr[nodeCnt++];
	}

	void insert(int idx, int cnt) {
		return;
	}

	void erase(int idx, int cnt) {
		if (idx == 0) {
			while (cnt-- > 0) {
				head = head->next;
			}
			return;
		}

		Node* cur = head;
		for (int i = 0; i < idx; i++) cur = cur->next;
		Node* anchor = cur;
		for (int i = 0; i < cnt; i++) cur = cur->next;
		anchor->next = cur->next;

	}

	void add(int data) {
		tail->next = getNewNode(data);
		tail = tail->next;
	}
};


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int T = 10;
	vector<int> input;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		input = vector<int>(N);
		for (int i = 0; i < N; i++) cin >> input[i];






	}
	
	return 0;
}
