#include<iostream>
#include<vector>
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

	void insert(int idx, int cnt, vector<int>& nums) {
		int stk = 0;
		if (idx == 0) {
			if (head != nullptr) {
				Node* newhead = getNewNode(nums[0]);
				newhead->next = head;
				head = newhead;
			}
			else {
				head = getNewNode(nums[0]);
			}
			stk = 1;
			idx = 1;
		}
		Node* cur = head;
		for (int i = 1; i < idx; i++) cur = cur->next;
		Node* anchor = cur->next;
		for (int i = stk; i < cnt; i++) {
			cur->next = getNewNode(nums[i]);
			cur = cur->next;
		}
		cur->next = anchor;
		if (anchor == nullptr) tail = cur;
		return;
	}

	void erase(int idx, int cnt) {
		Node* cur = head;
		if (idx == 0) {
			while (cnt-- > 0) {
				cur = cur->next;
			}
			head = cur;
			return;
		}
		for (int i = 0; i < idx; i++) cur = cur->next;
		Node* anchor = cur;
		for (int i = 0; i < cnt; i++) cur = cur->next;
		anchor->next = cur->next;
		if (anchor->next == nullptr) tail = anchor;
		return;
	}

	void add(int num) {
		tail->next = getNewNode(num);
		tail = tail->next;
		return;
	}

	void print() {
		Node* cur = head;
		for (int i = 0; i < 10; i++) {
			cout << cur->data << " ";
			cur = cur->next;
		}
		cout << "\n";
	}
};

int main(int argc, char** argv)
{
	int test_case;
	int T = 10;
	// freopen("input.txt", "r", stdin);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cout << "#" << test_case << " ";
		LinkedList llst;
		int N;
		cin >> N;
		vector<int> input_batch;
		input_batch = vector<int>(N);
		for (int i = 0; i < N; i++) cin >> input_batch[i];
		llst.insert(0, N, input_batch);
		int M;
		cin >> M;
		while (M--) {
			char cmd;
			int x, y;
			cin >> cmd;
			switch (cmd) {
			case 'I':
				cin >> x >> y;
				input_batch = vector<int>(y);
				for (int i = 0; i < y; i++) cin >> input_batch[i];
				llst.insert(x, y, input_batch);
				break;
			case 'D':
				cin >> x >> y;
				llst.erase(x, y);
				break;
			case 'A':
				cin >> y;
				for (int i = 0; i < y; i++) {
					int input;
					cin >> input;
					llst.add(input);
				}
				break;
			}
		}
		llst.print();
	}
	return 0;
}