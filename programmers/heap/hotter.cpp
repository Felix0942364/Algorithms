#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> pq = {};
    int answer = 0;
    for (int i : scoville) pq.push(i);
    while (pq.top() < K) {
        int i, j;
        if (!pq.empty()) {
            i = pq.top();
            pq.pop();
        } else {
            answer = -1;
            break;
        }
        if (!pq.empty()) {
            j = pq.top();
            pq.pop();
        } else {
            answer = -1;
            break;
        }
        pq.push(i+2*j);
        answer++;
    }    
    return answer;
}