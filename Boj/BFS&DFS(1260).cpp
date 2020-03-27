//
//  알고리즘.cpp
//  treee
//
//  Created by Apple on 2020/03/25.
//  Copyright © 2020 minjae. All rights reserved.
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int arr[100][100];


void DFS(int start, vector<int> graph[], bool check[]){
    check[start] = true;
    cout<<start<<" ";
    for(int i=0; i<graph[start].size(); i++){
        int next = graph[start][i];
        
        if(check[next] == false){
            DFS(next, graph, check);
        }
    }
}


void BFS(int start, vector<int> graph[], bool check[]){
    queue<int> q;
    
    q.push(start);
    check[start] = true;
    
    while(!q.empty()){
        int tmp = q.front();
        q.pop();
        cout<<tmp<<" ";
        
        for(int i=0; i<graph[tmp].size(); i++){
            if(check[graph[tmp][i]] == false){
                q.push(graph[tmp][i]);
                check[graph[tmp][i]] = true;
            }
        }
    }
}

int main()
{
    int n,m,start;
    cin>>n>>m>>start;
    
    vector<int> graph[1001];
    vector<int> copygraph[1001];
    bool check[1001];
    bool check2[1001];
    fill(check, check+n+1, false);
    fill(check2, check2+n+1, false);
    
    
    for(int i=0; i<m; i++){
        int u,v;
        
        cin>>u>>v;
        
        graph[u].push_back(v);
        graph[v].push_back(u);
        copygraph[u].push_back(v);
        copygraph[v].push_back(u);
    }
    
    for(int i=1; i<=n; i++){
        sort(graph[i].begin(), graph[i].end());
        sort(copygraph[i].begin(),copygraph[i].end());
    }
    
    DFS(start, graph, check);
    cout<<endl;
    BFS(start, copygraph, check2);
    cout<<endl;
    
    return 0;
}
