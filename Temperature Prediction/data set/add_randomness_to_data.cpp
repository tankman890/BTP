#include <bits/stdc++.h>

using namespace std;

int main() {

    ofstream newfile;
    ifstream f;

    f.open("data_without_randomness.csv");
    newfile.open("data_with_randomness.csv");

    string line;

    bool t = true;

    while(!f.eof()) {
        f >> line;

        if(t) {
            newfile << line;
            newfile << '\n';
            t = false;
        } else {
            stringstream ss(line);
            string word;
            int i = 1, v = 0;
            while (!ss.eof()) {
                getline(ss, word, ',');if(i == 4) {
                    //if(word.back() == '\n') word.pop_back();
                    int pred = stoi(word) + (rand() % 5 - 2);
                    word = to_string(pred) + '\n';
                } else {
                    word += ',';
                }
                i++;
                newfile << word;
            }
        }
    }

    return 0;
}