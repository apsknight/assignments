#include <bits/stdc++.h>
using namespace std;

class process{
public:
    int processID;
    int arrivalTime;
    bool running = false;
    queue<int> burst;
    queue<int> io;
    int completionTime;    
    bool ioStatus = false;
    process(vector<int> pin) {
        arrivalTime = pin[0];

        for(int i = 1; i < pin.size(); i++) {
            if (i&1) {
                burst.push(pin[i]);
            }
            else {
                io.push(pin[i]);
            }
        }
    }

    int getArrivalTime() {
        return arrivalTime;
    }

    int getNextBurst() {
        return burst.front();
    }

    void popBurst() {
        burst.pop();
    }

    int getNextIo() {
        return io.front();
    }

    void popIo() {
        io.pop();
    }

    bool burstAvail() {
        return burst.size() > 1;
    }

    bool ioAvail() {
        return io.size() > 1;
    }
};

int currentTime = 0;

class Compare{
public:
    bool operator() (process a, process b) {
        if (a.ioStatus || b.ioStatus) {
            return a.ioStatus;
        }
        if (a.getArrivalTime() > currentTime && b.getArrivalTime() > currentTime) {
            return false;
        }
        else if (a.getArrivalTime() > currentTime || b.getArrivalTime() > currentTime) {
            return a.getArrivalTime() > currentTime;
        }
        // else (a.getArrivalTime() <= currentTime && b.getArrivalTime() <= currentTime) {
        //     return 
        // }

        return a.getNextBurst() > b.getNextBurst(); 
    }
};

int main() {
    freopen("input.txt", "r", stdin);
    
    vector<process> prs;
    int inp;
    vector<int> pcr;
    while(cin >> inp) {
        if (inp == -1) {
            prs.push_back(process(pcr));
            pcr.clear();
        }
        else {
            pcr.push_back(inp);
        }
    }

    priority_queue<process, vector<process>, Compare> jobQueue;
    deque<process> ioQueue;
    for(auto p : prs) {
        jobQueue.push(p);
    }

    while(!jobQueue.empty() || !ioQueue.empty()) {
        if (!jobQueue.empty()) {
            process q = jobQueue.top();
            jobQueue.pop();
            q.burst.front()--;

            if (q.burst.front() == 0) {
                q.burst.pop();
                if (q.ioAvail()) {
                    ioQueue.push_back(q);
                }
            }
            else {
                cout << q.burst.front() << endl;
                jobQueue.push(q);
            }
        }


        if (ioQueue.size() != 0) {
            process r = ioQueue.front();
            ioQueue.pop_front();
            r.io.front()--;
            if (r.io.front() == 0) {
                r.io.pop();
                jobQueue.push(r);
            }
            else {
                ioQueue.push_front(r);
            }
        }
        currentTime++;
        cout << jobQueue.size() << " " << ioQueue.size() << endl;
    }
}