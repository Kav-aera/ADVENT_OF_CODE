#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm> 
using namespace std;

int main() {
    ifstream inputFile("input.txt");
    if (!inputFile) {
        cerr << "Error: Unable to open file.\n";
        return 1;
    }

    vector<int> leftList;   
    vector<int> rightList;  
    int left, right;

    
    while (inputFile >> left >> right) {
        leftList.push_back(left);
        rightList.push_back(right);
    }
    inputFile.close();

    
    sort(leftList.begin(), leftList.end());
    sort(rightList.begin(), rightList.end());

   
    vector<int> differences;
    for (int i = 0; i < leftList.size(); i++) {
        differences.push_back(abs(leftList[i] - rightList[i]));
    }

    int sum=0;
    for(int i=0;i<differences.size();i++) sum+=differences[i];
    cout<<sum;

    return 0;
}
