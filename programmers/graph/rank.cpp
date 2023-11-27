#include <iostream>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    vector<vector<bool>> graph(n, vector<bool>(n, false));

    for(auto& result : results) {
        graph[result[0]-1][result[1]-1] = true;
    }

    for(int k = 0; k < n; k++) {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(graph[i][k] && graph[k][j]) {
                    graph[i][j] = true;
                }
            }
        }
    }

    int answer = 0;
    for(int i = 0; i < n; i++) {
        int count = 0;
        for(int j = 0; j < n; j++) {
            if(graph[i][j] || graph[j][i]) count++;
        }
        if(count == n-1) answer++;
    }

    return answer;
}

