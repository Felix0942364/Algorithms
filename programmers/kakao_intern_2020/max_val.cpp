#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<char> op_set {'+', '-', '*'}; // used operands are + - *

long long calculate(long long a, long long b, char op) { // calculate helper function
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
    while (pos < expression.size()) { // decode expression to integer and operator
        if (isdigit(expression[pos])) { 
            values.push_back(stoll(expression.substr(pos))); // vector pushback, string to longlong, string substring
            pos += to_string(values.back()).size(); // add last added value size
        }
        else {
            operators.push_back(expression[pos]); 
            pos++; // add 1 since single operation counts as 1 character
        }
    }

    for (char op : ops) { // run each operation in the order as predefined permutation
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
    int len = op_set.size(); // length of operator set
    sort(op_set.begin(), op_set.end()); // sorting is needed in order for all permutation to work
    do {
        long long result = evaluateExpression(expression, op_set);
        answer = max(answer, result);
    } while (next_permutation(op_set.begin(), op_set.end()));
    return answer;
}
