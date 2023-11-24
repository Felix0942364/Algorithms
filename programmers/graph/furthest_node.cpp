#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    vector<vector<int>> graph(20000, vector<int> {});
    for (vector<int> pair: edge) {
        graph[pair[0]].push_back(pair[1]);
        graph[pair[1]].push_back(pair[0]);
    }
    vector<bool> visited(20000, false);
    set<int> s = {1};
    visited[1] = true;
    while (!s.empty()) {
        set<int> tmp = {};
        for (int copy:s) tmp.insert(copy);
        s.clear();
        for (int curr_node:tmp) {
            for(int next_node:graph[curr_node]) {
                if (visited[next_node]) {
                    continue;
                }
                else {
                    visited[next_node] = true;
                    s.insert(next_node);
                }
            }
        }
        if (!s.empty()) answer = s.size();
    }
    return answer;
}