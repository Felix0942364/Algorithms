#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Job {
    int start, duration;
    Job(int s, int d) : start(s), duration(d) {}
    bool operator<(const Job& other) const {
        return start > other.start;
    }
};

int solution(vector<vector<int>> jobs) {
    priority_queue<Job> jobsQueue;
    for (const auto& job : jobs) {
        jobsQueue.emplace(job[0], job[1]);
    }
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> waitQueue;
    int count = 0, currentTime = 0, totalWaitTime = 0;

    while (count < jobs.size()) {
        while (!jobsQueue.empty() && jobsQueue.top().start <= currentTime) {
            auto job = jobsQueue.top();
            jobsQueue.pop();
            waitQueue.emplace(job.duration, job.start);
        }

        if (!waitQueue.empty()) {
            auto job = waitQueue.top();
            waitQueue.pop();

            currentTime += job.first;
            totalWaitTime += currentTime - job.second;
            count++;
        } else {
            if (!jobsQueue.empty()) {
                currentTime = jobsQueue.top().start;
            }
        }
    }

    return totalWaitTime / jobs.size();
}