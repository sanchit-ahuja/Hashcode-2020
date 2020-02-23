#include<bits/stdc++.h>
#include<fstream>

using namespace std;
vector<int> scores;

bool comparePairs(const int a, const int b)
{
  return scores[a] > scores[b];
}

int main () {
    ifstream file;
    ofstream ofile;
    file.open("f_libraries_of_the_world.txt");
    ofile.open("hashcode_f_sol.txt");
    int books, libs, days;
    int score;
    file>>books>>libs>>days;
    for (int k=0; k<books; k++) {
        file>>score;
        scores.push_back(score);
    }

    multimap<double, vector<vector<int> >, greater<int> > m;
    multimap<double, vector<vector<int> >, greater<int> >::iterator it;
    pair<double, vector<vector<int> > > p;
    int a, b, c, d, i = 0;
    cout<<"\n\n-- Reading from file --\n\n";
    while (file>>a) {
        file>>b;
        file>>c;
        p = make_pair((double)(pow(a,0.5)*c)/(double)(b), vector<vector<int> >(2, vector<int>(0,0)));
        p.second[0].push_back(a);
        p.second[0].push_back(b);
        p.second[0].push_back(c);
        p.second[0].push_back(i);

        for (int k=0; k<a; k++) {
            file>>d;
            p.second[1].push_back(d);
        }
        sort(p.second[1].begin(), p.second[1].end(), comparePairs);
        m.insert(p);
        i++;
    }
    cout<<"\n\n-- Read from file -- \n\n";
    int day = 0;
    int count = 0;
    map<int, int> s;
    for (it = m.begin(); it != m.end(); it++) {
        day += (*it).second[0][1];
        if (day>=days)
            break;
        count++;
        vector<int> v;
        for (int j=0; j<(*it).second[0][0]; j++) {
            if (s.find((*it).second[1][j]) == s.end()) {
                v.push_back((*it).second[1][j]);
                s.insert(make_pair((*it).second[1][j], 0));
            }
        }
        ofile<<(*it).second[0][3]<<" "<<v.size()<<endl;
        for (int j=0; j<v.size(); j++)
            ofile<<v[j]<<" ";
        ofile<<endl;
    }

    cout<<count<<endl;
    file.close();
    ofile.close();
    return 0;
}