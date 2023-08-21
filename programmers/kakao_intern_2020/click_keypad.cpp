#include <string>
#include <vector>

using namespace std;
struct Pair {
    int row;
    int col;
};

vector<Pair> map {
    {3,1}, 
    {0,0}, {0,1}, {0,2},
    {1,0}, {1,1}, {1,2},
    {2,0}, {2,1}, {2,2}
};

char getHand(int num, string hand, Pair &left, Pair &right) {
    Pair newpoint = map[num];
    if (num == 1 || num == 4 || num == 7) {
        left = newpoint;
        return 'L';
    }
    else if (num == 3 || num == 6 || num == 9) {
        right = newpoint;
        return 'R';
    }
    int range_left = abs(newpoint.row - left.row) + abs(newpoint.col - left.col);
    int range_right = abs(newpoint.row - right.row) + abs(newpoint.col - right.col);
    if (range_left < range_right) {
        left = newpoint;
        return 'L';
    } else if (range_left > range_right) {
        right = newpoint;
        return 'R';
    } else if (hand == "left") {
        left = newpoint;
        return 'L';
    } else {
        right = newpoint;
        return 'R';
    }
}

string solution(vector<int> numbers, string hand) {
    string answer = "";
    Pair left = {3,0};
    Pair right = {3,2};
    for (int num: numbers) {
        answer.push_back(getHand(num, hand, left, right));
    }
    return answer;
}