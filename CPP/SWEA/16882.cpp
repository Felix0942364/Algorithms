#include<iostream>

using namespace std;
int arr[6];
bool result;

bool change(int i, int j) {
	int tmp = arr[i];
	arr[i] = arr[j];
	arr[j] = tmp;
	return true;
}

bool validate() {
	for (int i = 0; i < 6; i++);
	if (arr[0] == arr[1] && arr[1] == arr[2]) {
		if (arr[3] + 2 == arr[4] + 1 && arr[4] + 1 == arr[5]) {
			result = true;
		}
		else if (arr[3] == arr[4] && arr[4] == arr[5]) {
			result = true;
		}
	}
	else if (arr[0] + 2 == arr[1] + 1 && arr[1] + 1 == arr[2] + 2) {
		if (arr[3] + 2 == arr[4] + 1 && arr[4] + 1 == arr[5]) {
			result = true;
		}
		else if (arr[3] == arr[4] && arr[4] == arr[5]) {
			result = true;
		}
	}
	return false;
}

bool perm(int i, int k) {
	if (i == k) {
		validate();
	}
	else {
		for (int j = i; j < k; j++) {
			change(i, j);
			perm(i + 1, k);
			change(i, j);
		}
	}
	return false;
}

int pow(int a) {
	int t = 1;
	for (int i = 0; i < a; i++) {
		t = t * 10;
	}
	return t;
}

int main() {
	int T;
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		int input;
		result = false;
		cin >> input;
		for (int i = 0; i < 6; i++) {
			arr[i] = (input / pow(i)) % 10;
		}
		perm(0, 6);
		if (result) cout << "True" << "\n";
		else cout << "False" << "\n";
	}
	return 0;
}
