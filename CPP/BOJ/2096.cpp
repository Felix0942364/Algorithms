#include <iostream>

using namespace std;
constexpr int MAX_SUM = 900000;

int min(int *arr) {
	int tmp = arr[0];
	for (int i = 1; i < 3; i++) {
		tmp = arr[i] < tmp ? arr[i] : tmp;
	}
	return tmp;
}

int max(int* arr) {
	int tmp = arr[0];
	for (int i = 1; i < 3; i++) {
		tmp = arr[i] > tmp ? arr[i] : tmp;
	}
	return tmp;
}

int main() {
	int N;
	cin >> N;
	int input[3], prior_mn[3], prior_mx[3];
	for (int i = 0; i < 3; i++) {
		cin >> input[i];
		prior_mn[i] = input[i];
		prior_mx[i] = input[i];
	}
	while (N-- > 1) {
		for (int i = 0; i < 3; i++) cin >> input[i];
		int cur_mn[3] = { MAX_SUM, MAX_SUM, MAX_SUM };
		int cur_mx[3] = { 0, 0, 0 };
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if ((i == 0 && j == 2) || (i == 2 && j == 0)) continue;
				cur_mn[i] = cur_mn[i] < input[i] + prior_mn[j] ? cur_mn[i] : input[i] + prior_mn[j];
				cur_mx[i] = cur_mx[i] > input[i] + prior_mx[j] ? cur_mx[i] : input[i] + prior_mx[j];
			}
		}
		for (int i = 0; i < 3; i++) {
			prior_mn[i] = cur_mn[i];
			prior_mx[i] = cur_mx[i];
		}
	} 
	cout << max(prior_mx) << " " << min(prior_mn);
}