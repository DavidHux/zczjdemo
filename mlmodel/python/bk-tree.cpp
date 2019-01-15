// C++ program to demonstrate working of BK-Tree
// #include "bits/stdc++.h"
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <filesystem>

using namespace std;

// maximum number of words in dict[]
#define MAXN 2200

// defines the tolerence value
#define TOL 1

// defines maximum length of a word
#define LEN 100

struct Node
{
    // stores the word of the current Node
    string word;
    string id;

    // links to other Node in the tree
    int next[2 * LEN];

    // constructors
    Node(string x, string y) : word(x), id(y)
    {
        // initializing next[i] = 0
        for (int i = 0; i < 2 * LEN; i++)
            next[i] = 0;
    }
    Node() : word(""), id("") {}
};

// stores the root Node

int min(int a, int b, int c)
{
    return min(a, min(b, c));
}

// Edit Distance
// Dynamic-Approach O(m*n)
int editDistance(string &a, string &b)
{
    if (a.size() >= 100 || b.size() >= 100)
        cout << "error" << a << ' ' << b << endl;
    int m = a.length(), n = b.length();
    int dp[m + 1][n + 1];

    // filling base cases
    for (int i = 0; i <= m; i++)
        dp[i][0] = i;
    for (int j = 0; j <= n; j++)
        dp[0][j] = j;

    // populating matrix using dp-approach
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (a[i - 1] != b[j - 1])
            {
                dp[i][j] = min(1 + dp[i - 1][j],    // deletion
                               1 + dp[i][j - 1],    // insertion
                               1 + dp[i - 1][j - 1] // replacement
                );
            }
            else
                dp[i][j] = dp[i - 1][j - 1];
        }
    }
    return dp[m][n];
}

// adds curr Node to the tree
void add(Node &root, Node &curr, Node &RT, Node tree[], int &ptr)
{
    if (root.word == "")
    {
        // if it is the first Node
        // then make it the root Node
        root = curr;
        return;
    }

    // get its editDist from the Root Node
    int dist = editDistance(curr.word, root.word);

    if (tree[root.next[dist]].word == "")
    {
        /* if no Node exists at this dist from root 
		* make it child of root Node*/

        // incrementing the pointer for curr Node
        ptr++;

        // adding curr Node to the tree
        tree[ptr] = curr;

        // curr as child of root Node
        root.next[dist] = ptr;
    }
    else
    {
        // recursively find the parent for curr Node
        add(tree[root.next[dist]], curr, RT, tree, ptr);
    }
}

vector<pair<string, string>> getSimilarWords(Node &root, string &s, Node tree[])
{
    vector<pair<string, string>> ret;
    if (root.word == "")
        return ret;

    // calculating editdistance of s from root
    int dist = editDistance(root.word, s);

    // if dist is less than tolerance value
    // add it to similar words
    if (dist <= TOL)
        ret.push_back(pair<string, string>(root.word, root.id));

    // iterate over the string havinng tolerane
    // in range (dist-TOL , dist+TOL)
    int start = dist - TOL;
    if (start < 0)
        start = 0;

    while (start < dist + TOL)
    {
        vector<pair<string, string>> tmp =
            getSimilarWords(tree[root.next[start]], s, tree);
        for (auto i : tmp)
            ret.push_back(i);
        start++;
    }
    return ret;
}

string findnth(string m, char s, int n)
{
    int a = 0;
    int prevpos = 0;
    for (int i = 0; i < m.length(); i++)
    {
        if (m[i] == s)
        {
            if (a == n)
            {
                return m.substr(prevpos + 2, i - prevpos - 3);
            }
            else
            {
                a++;
                prevpos = i;
            }
        }
    }
    cout << "addr not find: " + m << endl;
    return "";
}

vector<pair<string, string>> readaddr(string filename)
{
    vector<pair<string, string>> ret;
    ifstream f(filename);
    string l, addr;
    while (getline(f, l))
    {
        addr = findnth(l, ',', 32);
        // cout<<l<<endl;
        string id = l.substr(1, l.find(',') - 2);
        // cout<<id<<endl;
        if (addr.length() > 5 && addr.length() < 100)
            ret.push_back(pair<string, string>(addr, id));
    }
    return ret;
}

// driver program to run above functions
int main(int argc, char const *argv[])
{
    string path = "data/addr";
    ofstream outfile("data/simaddrs.txt");
    for (auto &p : filesystem::directory_iterator(path))
    {
        // cout << p << endl;
        // continue;
        Node *RT = new Node;
        // stores every Node of the tree
        Node *tree = new Node[MAXN];
        // index for current Node of tree
        int ptr = 0;
        string patha = p.path().string();
        vector<pair<string, string>> addrs = readaddr(patha);
        int sz = addrs.size();
        // cout << sz << endl;

        // adding dict[] words on to treeb
        for (int i = 0; i < sz; i++)
        {
            Node tmp = Node(addrs[i].first, addrs[i].second);
            add(*RT, tmp, *RT, tree, ptr);
        }

        vector<pair<pair<string, string>, pair<string, string>>> sim;
        // string w1 = "济南市历下区天辰大街603号";
        // string w2 = "济南市历下区山大路239号";
        for (auto x : addrs)
        {
            vector<pair<string, string>> match = getSimilarWords(*RT, x.first, tree);
            for (auto y : match)
            {
                if (y.second != x.second)
                    sim.push_back(pair<pair<string, string>, pair<string, string>>(x, y));
            }
        }
        for (auto x : sim)
        {
            if (x.first.first.find_first_of("0123456789") != string::npos)
                outfile << x.first.first << " " << x.first.second << "  " << x.second.first << " " << x.second.second << endl;
        }
        delete RT;
        delete[] tree;
    }

    return 0;
}
