#include <string>
#include <vector>

using namespace std;
struct Pair { // structure for coordinates
    int row;
    int col;
};

vector<Pair> map { // mapping number to coordinates
    {3,1}, 
    {0,0}, {0,1}, {0,2},
    {1,0}, {1,1}, {1,2},
    {2,0}, {2,1}, {2,2}
};

char getHand(int num, string hand, Pair &left, Pair &right) {
    Pair newpoint = map[num];
    if (num == 1 || num == 4 || num == 7) { // highest priority left hand 1,4,7
        left = newpoint;
        return 'L';
    }
    else if (num == 3 || num == 6 || num == 9) { // highest priority right hand 3,6,9
        right = newpoint;
        return 'R';
    }
    int range_left = abs(newpoint.row - left.row) + abs(newpoint.col - left.col); // for manhattan distance
    int range_right = abs(newpoint.row - right.row) + abs(newpoint.col - right.col);
    if (range_left < range_right) { // compare left right range
        left = newpoint;
        return 'L';
    } else if (range_left > range_right) {
        right = newpoint;
        return 'R';
    } else if (hand == "left") { // left hander
        left = newpoint;
        return 'L';
    } else {
        right = newpoint;
        return 'R';
    }
}

string solution(vector<int> numbers, string hand) {
    string answer = "";
    Pair left = {3,0}; // initial coord
    Pair right = {3,2};
    for (int num: numbers) {
        answer.push_back(getHand(num, hand, left, right));
    }
    return answer;
}