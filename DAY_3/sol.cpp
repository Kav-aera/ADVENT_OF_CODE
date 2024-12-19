#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

int processString(const string& inputStr) {
    int sumTotal = 0;
    size_t pos = 0;

    while (true) {
        pos = inputStr.find("mul(", pos);
        if (pos == string::npos)
            break;

        size_t start = pos + 4;
        if (start >= inputStr.size())
            break;

        int parenCount = 1;
        size_t end = start;

        while (end < inputStr.size() && parenCount > 0) {
            if (inputStr[end] == '(')
                parenCount++;
            if (inputStr[end] == ')')
                parenCount--;
            if (parenCount > 0)
                end++;
        }

        if (parenCount == 0) {
            string nums = inputStr.substr(start, end - start);

            size_t commaPos = nums.find(',');
            if (commaPos != string::npos) {
                string num1Str = nums.substr(0, commaPos);
                string num2Str = nums.substr(commaPos + 1);

                num1Str.erase(0, num1Str.find_first_not_of(" \t"));
                num1Str.erase(num1Str.find_last_not_of(" \t") + 1);
                num2Str.erase(0, num2Str.find_first_not_of(" \t"));
                num2Str.erase(num2Str.find_last_not_of(" \t") + 1);

                bool validNum1 = !num1Str.empty() && all_of(num1Str.begin(), num1Str.end(), ::isdigit);
                bool validNum2 = !num2Str.empty() && all_of(num2Str.begin(), num2Str.end(), ::isdigit);

                if (validNum1 && validNum2) {
                    int num1 = stoi(num1Str);
                    int num2 = stoi(num2Str);
                    sumTotal += num1 * num2;
                }
            }

            pos = end + 1;
        } else {
            pos = start;
        }
    }

    return sumTotal;
}

pair<int, string> processFile(const string& filePath) {
    try {
        ifstream file(filePath);
        if (!file.is_open())
            return {0, "Error: Could not find or open file at " + filePath};

        string content((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
        int result = processString(content);
        return {result, ""};
    } catch (const exception& e) {
        return {0, "Error: An unexpected error occurred: " + string(e.what())};
    }
}

int main() {
    string filePath = "c:\\PROJECTS\\ADVENT_OF_CODE\\DAY_3\\input.txt";
    auto [result, error] = processFile(filePath);

    if (!error.empty()) {
        cerr << error << endl;
    } else {
        cout << "The result of processing the file is: " << result << endl;
    }

    return 0;
}
