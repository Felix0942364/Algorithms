#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<char> op_set {'+', '-', '*'};

long long calculate(long long a, long long b, char op) {
    if (op == '+')
        return a + b;
    else if (op == '-')
        return a - b;
    else if (op == '*')
        return a * b;
    return 0;
}

long long evaluateExpression(const string& expression, const vector<char>& ops) {
    vector<long long> values;
    vector<char> operators;
    size_t pos = 0;
    while (pos < expression.size()) {
        if (isdigit(expression[pos])) {
            values.push_back(stoll(expression.substr(pos)));
            pos += to_string(values.back()).size();
        }
        else {
            operators.push_back(expression[pos]);
            pos++;
        }
    }
    for (char op : ops) {
        vector<long long> new_values;
        vector<char> new_operators;
        for (size_t i = 0; i < operators.size(); i++) {
            if (operators[i] == op) {
                long long result = calculate(values[i], values[i + 1], op);
                values[i + 1] = result;
            }
            else {
                new_values.push_back(values[i]);
                new_operators.push_back(operators[i]);
            }
        }
        new_values.push_back(values.back());
        values = new_values;
        operators = new_operators;
    }
    return abs(values.front());
}

long long solution(string expression) {
    long long answer = 0;
    int len = op_set.size();
    sort(op_set.begin(), op_set.end());
    do {
        long long result = evaluateExpression(expression, op_set);
        answer = max(answer, result);
    } while (next_permutation(op_set.begin(), op_set.end()));
    return answer;
}
