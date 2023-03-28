#include <iostream>

using namespace std;

int result = 0;

int pow(int i) {
	int temp = 1;
	while (i--) temp = temp * 10;
	return temp;
}

int sum(int set[], int size) {
	int sum = 0;
	while (size--) {
		sum += set[size] * pow(size);
	}
	return sum;
}

int flip(int set[], int size, int cnt, int max_cnt) {
	if (cnt == max_cnt) {
		if (result < sum(set, size)) result = sum(set, size);
		return 0;
	}
	else
		for (int i = 0; i < size - 1; i++) {
			for (int j = i + 1; j < size; j++) {
				int temp = set[i];
				set[i] = set[j];
				set[j] = temp;
				flip(set, size, cnt + 1, max_cnt);
				temp = set[i];
				set[i] = set[j];
				set[j] = temp;
			}
		}
	return 0;
}

int main() {
	int T;
	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {
		int input, change;
		int size = 0;
		int arr[6] = {};
		int cnt = 0;
		result = 0;
		cin >> input >> change;
		for (int i = 0; i < 6; i++) {
			if (int temp = input / pow(i)) {
				arr[i] = (temp) % 10;
				size++;
			}
			else break;
		}
		if (change > 6) {
			while (change--) {
				int local_max[6] = {};
				for (int i = 0; i < size - 1; i++) {
					for (int j = i + 1; j < size; j++) {
						int temp[6];
						for (int k = 0; k < size; k++) temp[k] = arr[k];
						int tmp = temp[i];
						temp[i] = temp[j];
						temp[j] = tmp;
						if (sum(temp, size) > sum(local_max, size)) {
							for (int k = 0; k < size; k++) local_max[k] = temp[k];
						}
					}
				}
				for (int i = 0; i < size; i++) arr[i] = local_max[i];
			}
			result = sum(arr, size);
		}
		else {
			flip(arr, size, cnt, change);
		}
		cout << "#" << test_case << " " << result << endl;
	}
	return 0;
}