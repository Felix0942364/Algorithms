#include <string>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> operations) {
    priority_queue<int> mx_q;
    priority_queue<int, vector<int>, greater<>> mn_q;
    unordered_map<int, int> count;

    for (string op : operations) {
        char command = op[0];
        int number = stoi(op.substr(2));

        if (command == 'I') {
            mx_q.push(number);
            mn_q.push(number);
            count[number]++;
        } else {
            if (command == 'D' && number == 1) {
                while (!mx_q.empty() && count[mx_q.top()] == 0) mx_q.pop();
                if (!mx_q.empty()) {
                    count[mx_q.top()]--;
                    mx_q.pop();
                }
            } else if (command == 'D' && number == -1) {
                while (!mn_q.empty() && count[mn_q.top()] == 0) mn_q.pop();
                if (!mn_q.empty()) {
                    count[mn_q.top()]--;
                    mn_q.pop();
                }
            }
        }
    }

    while (!mx_q.empty() && count[mx_q.top()] == 0) mx_q.pop();
    while (!mn_q.empty() && count[mn_q.top()] == 0) mn_q.pop();

    if (mx_q.empty() || mn_q.empty()) return {0, 0};
    return {mx_q.top(), mn_q.top()};
}
