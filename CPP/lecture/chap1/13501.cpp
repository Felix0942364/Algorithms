#include<iostream>
#include<vector>
#define MAX_NODE 10000
using namespace std;

struct Node {
	int data;
	Node* next;
	Node(int data) : data(data), next(nullptr) {}
};

class LinkedList {
private:
	Node* head;
	vector<Node*> nodePool;
	int node_count;
public:
	LinkedList() : head(nullptr), node_count(0) {
		nodePool.resize(MAX_NODE, nullptr);
	}

	Node* getNode(int data) {
		nodePool[node_count] = new Node(data);
		return nodePool[node_count++];
	}

	void insert(int idx, int val) {
		if (head == nullptr) {
			head = getNode(val);
			return;
		}
		Node* cur = head;
		while (idx-- > 1) cur = cur->next;
		Node* new_node = getNode(val);
		new_node->next = cur->next;
		cur->next = new_node;
	}

	void erase(int idx) {
		if (idx == 0) {
			head = head->next;
			return;
		}
		Node* cur = head;
		while (idx-- > 1) cur = cur->next;
		cur->next = cur->next->next;
	}

	void change(int idx, int val) {
		Node* cur = head;
		while (idx-- > 0) cur = cur->next;
		cur->data = val;
	}

	int value(int idx) {
		int answer = -1;
		Node* cur = head;
		for (int i = 0; i < idx; i++) {
			if (cur->next == nullptr) return answer;
			cur = cur->next;
		}
		answer = cur->data;
		return answer;
	}
};

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(NULL);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int test_case;
	int T;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cout << "#" << test_case << " ";
		LinkedList llst;
		int N, M, L;
		cin >> N >> M >> L;
		int x, y;
		for (int i = 0; i < N; i++) {
			cin >> y;
			llst.insert(i, y);
		}

		while (M-- > 0) {
			char cmd;
			cin >> cmd;
			switch (cmd) {
			case 'I':
				cin >> x >> y;
				llst.insert(x, y);
				break;
			case 'D':
				cin >> x;
				llst.erase(x);
				break;
			case 'C':
				cin >> x >> y;
				llst.change(x, y);
				break;
			}
		}
		cout << llst.value(L) << "\n";
	}
	return 0;
}