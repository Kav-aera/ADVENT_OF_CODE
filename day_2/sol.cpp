#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

bool is_ascending(const vector<int>& arr) {
    for (int i = 0; i < arr.size() - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}

bool is_descending(const vector<int>& arr) {
    for (int i = 0; i < arr.size() - 1; i++) {
        if (arr[i] < arr[i + 1]) {
            return false;
        }
    }
    return true;
}

bool check_order(const vector<int>& arr) {
    if (is_ascending(arr) || is_descending(arr)) {
        for (int i = 0; i < arr.size() - 1; i++) {
            int diff = abs(arr[i] - arr[i + 1]);
            if (diff > 3 || diff == 0) {
                return false;
            }
        }
        return true;
    }
    return false;
}

bool can_be_safe_by_removal(const vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        vector<int> temp = arr;
        temp.erase(temp.begin() + i); // Remove one element

        if (is_ascending(temp) || is_descending(temp)) {
            for (int j = 0; j < temp.size() - 1; j++) {
                int diff = abs(temp[j] - temp[j + 1]);
                if (diff > 3 || diff == 0) {
                    return false;
                }
            }
            return true; // Safe after removal
        }
    }
    return false; // Not safe after any removal
}

int main() {
    ifstream file("input.txt");

    if (!file) {
        cout << "Could not open file." << endl;
        return 1;
    }

    vector<int> arr;
    int num;
    int count = 0;

    while (file >> num) {
        arr.push_back(num);

        if (file.peek() == '\n' || file.eof()) {
            // Check if the array is already safe or can be made safe by removal
            if (check_order(arr) || can_be_safe_by_removal(arr)) {
                count++;
            }
            arr.clear();
        }
    }

    cout << count << endl;

    return 0;
}
