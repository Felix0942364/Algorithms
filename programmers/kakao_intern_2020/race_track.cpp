#include <iostream>
#include <string>
#include <vector>
#include <queue>
#define MAX_VAL 999999

using namespace std;

struct Node {
    int row, col, dir, val;
};

struct CompareNode {
    bool operator() (const Node& a, const Node& b) {
        return a.val < b.val;
    }
};

int map[25][25][4];
int dr[4] = { 1, 0, -1, 0 };
int dc[4] = { 0, 1, 0, -1 };

int solution(vector<vector<int>> board) {
    for (int i = 0; i < 25; i++) {
        for (int j = 0; j < 25; j++) {
            for (int k = 0; k < 4; k++)
                map[i][j][k] = MAX_VAL;
        }
    }
    for (int i = 0; i < 4; i++) map[0][0][i] = 0;
    int size = board.size();
    priority_queue<Node, vector<Node>, CompareNode> pq;
    pq.push({0,0,0,0});
    pq.push({0,0,1,0});
    while (!pq.empty()) {
        Node cur = pq.top();
        pq.pop();
        for (int i = 0; i < 4; i++) {
            int nr = cur.row + dr[i];
            int nc = cur.col + dc[i];
            if (nr < 0 || nr >= size || nc < 0 || nc >= size) continue;
            if (board[nr][nc] == 1) continue;
            int nv = cur.val;
            if (cur.dir % 2 == i % 2) nv += 100;
            else nv += 600;
            if (map[nr][nc][i] <= nv) continue;
            map[nr][nc][i] = nv;
            pq.push({ nr, nc, i, nv });
        }
    }
    int answer = MAX_VAL;
    for (int i : map[size - 1][size - 1]) {
        answer = min(i, answer);
    }
    return answer;
}