#include<iostream>
#include<string>

using namespace std;

int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
	int test_case;
	int T;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int N, M;
		cin >> N >> M;
		int check = (1 << N) - 1;
		string res = (check == (M & check)) ? "ON" : "OFF";
		cout << "#" << test_case << " " << res << "\n";
	}
	return 0;
}