#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

class Graph
{
public:
	Graph(int n);
	~Graph();
	bool loadInfo(string input);
	bool buildGraph();
	bool writeResult(string output);
private:
	int N;                          // 用户数
	vector<double> user;            // 话题下用户
	vector<double>* fans;           // 每个用户分别的 粉丝/关注
	int** A;                        // 邻接矩阵A(i,j)=1代表两人有 粉丝/关注 关系
	int count;
};
Graph::Graph(int n) {
	N = n;
	count = 0;
	fans = new vector<double>[N];
	A = new int*[N];
	for (int i = 0; i < N; i++)
		A[i] = new int[N];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			A[i][j] = 0;
		}
	}
}
Graph::~Graph() {
	delete[]fans;
	for (int i = 0; i < N; i++)
		delete[]A[i];
	delete[]A;
}
bool Graph::loadInfo(string input) {
	ifstream fin;
	fin.open(input.c_str(), std::ios::in);
	if (!fin) {
		std::cout << input << std::endl;
		std::cerr << "File cann't be opened!\n";
		return false;
	}
	double id;
	string line;
	std::getline(fin, line);
	int flag = 0;
	while (!line.empty()) {
		flag++;
		istringstream in(line);
		in >> id;
		user.push_back(id);
		in >> id;
		char c;
		double temp = id;
		while ((c = in.get()) != -1) {
			if (id != 0) {
				fans[count].push_back(id);
			}
			in >> id;
		}
		count++;
		getline(fin, line);
	}
	fin.close();
	return true;
}
bool Graph::buildGraph() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < fans[i].size(); j++) {
			for (int k = 0; k < N; k++) {
				if (fans[i][j] == user[k]) {
					A[i][k] = 1;        // 粉丝列表：k关注了i or 关注列表：i关注了k
					break;
				}
			}
		}
	}
	return true;
}
bool Graph::writeResult(string output) {
	ofstream fout;
	string edge = output + "_edge.csv";
	//string node = output + "_node.csv";
	fout.open(edge.c_str(), ios::out);
	fout << "source" << "," << "target" << endl;
	for (int i = 0; i < N; i++) {
		for (int k = 0; k < N; k++) {
			if (A[i][k] == 1) {
				fout << fixed << setprecision(0) << user[i] << "," << user[k] << endl;
			}
		}
	}
	/*for (int i = 0; i < N; i++) {
		fout << fixed << setprecision(0) << user[i] << "," << user[i] << endl;
	}*/
	fout.close();
	return true;
}
void main()
{
	string input = "lyzzr_follow_ming.txt";
	string output = "lyzzr_follow_ming";
	Graph g(3222);
	g.loadInfo(input);
	g.buildGraph();
	g.writeResult(output);
}


