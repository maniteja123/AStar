#include <bits/stdc++.h>
using namespace std;

struct Node {
	int x, y, f, g, h, a, b;

	bool operator<(const Node &a) const {
		return f > a.f ;
	}
};

struct Node board[100][100];
int path[100][100];
bool closed[100][100];
priority_queue <Node> opened;

void addnode(int x, int y, int g, int N) {
	int f, h;
	if( !(closed[x][y]) && x>=1 && x<=N && y>=1 && y<=N) {
		h = board[x][y].h ;
		f = g + h ;
		board[x][y].g = g;
		board[x][y].f = f;
		closed[x][y] = true;
		//cout << x <<" "<< y << " " << board[x][y].f <<  endl;
		opened.push(board[x][y]);
	}
}

void A_star( pair<int,int> start, pair<int,int> goal , int N) {
	bool lost = false, found = false;
	int i, j, f, go, g, h, x, y, type, jump, count=0 ;
	Node next;
	x = start.first;
	y = start.second;
	board[x][y].g = 0;
	g = go = 0;
	opened.push(board[x][y]);
	while (!found && !lost) {
		if(opened.size()==0) {
			lost = true;
		} else{
		    next = opened.top();
			opened.pop();
			x = next.x;
			y = next.y;
			if(next.g != go || go==0)
				cout  << x <<" "<< y << endl;
			go = next.g;
			path[x][y] = count ;
			count ++;
			g = next.g + 1;
			if(x==goal.first && y==goal.second) {
				found = true;
			} else {
				type = board[x][y].a;
				jump = board[x][y].b;
				if(!type){ 						// type == 0
					for(i=1; i<=jump+1; i++) {
						addnode(x, y+i, g, N);
						addnode(x+i, y, g, N);
						addnode(x, y-i, g, N);
						addnode(x-i, y, g, N);
					}
				} else { 						// type == 1 or type == -1
					addnode(x, y + type * (jump+1), g, N);
					addnode(x + type * (jump+1), y, g, N);
				}
			}
		}
	}
	if(found) {
		for(i=1; i<=N; i++){
        	for(j=1; j<=N; j++){
        		cout << path[i][j] << " ";
        	}
        	cout << endl;
        }
		printf("YES");
	} else if(lost) {
		printf("NO");
	}
    return ;
}

int main() {
    int N, T, i, j, x, y;
    scanf("%d", &N);
    pair <int, int> start, goal;
    start = make_pair(1,1);
    goal = make_pair(N,N);
    for(i=1; i<=N; i++){
        for(j=1; j<=N; j++){
            scanf("%d %d", &(board[i][j].a), &(board[i][j].b));
            board[i][j].h = (N-i)+(N-j);
            board[i][j].x = i;
            board[i][j].y = j;
            board[i][j].f = board[i][j].g = 0;
        }
    }
    A_star(start, goal, N);
    return 0;
}
