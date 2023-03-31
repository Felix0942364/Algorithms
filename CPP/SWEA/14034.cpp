#include <iostream>

using namespace std;
int N, B;
int list[20];
int result;

void dfs(int idx,int sum) {
  if (sum >= B){
    result = (sum < result)? sum:result;
    return;
  }
  for (int j=idx+1; j < N; j++) {
    dfs(j, sum + list[j]);
  }
}

int main()
{
	int T;
	cin >> T;
	for (int test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N >> B;
		result = 200000;
		for (int i = 0; i < N; i++) {
			cin >> list[i];
		}
    dfs(0,0);
		cout << "#" << test_case << " " << result << endl;
	}
	return 0;
}