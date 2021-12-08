#include <vector>
#include <iostream>
using namespace std;
int dy[4] = {0, -1, 0, 1};
int dx[4] = {-1, 0, 1, 0};
int tmp = 0;
void dfs(int y, int x, int visit[][101], vector<vector<int>> picture, int m, int n){
    for (int idx = 0; idx < 4; idx++){
        int ny = y + dy[idx];
        int nx = x + dx[idx];
        if (ny < 0 or ny >= m or nx < 0 or nx >= n) continue;
        if (picture[ny][nx] == picture[y][x] and visit[ny][nx] == 0){
            visit[ny][nx] = 1;
            tmp += 1;
            dfs(ny, nx, visit, picture, m, n);
        }
    }
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int visit[101][101];
    for (int i = 0; i < 101; i++){
        for(int j = 0; j < 101; j++){
            visit[i][j] = 0;
        }
    }
    for (int i = 0; i < m; i++){
        for (int j = 0 ; j < n ; j++){
            if (picture[i][j] != 0 and visit[i][j] == 0){
                visit[i][j] = 1;
                tmp = 1;
                dfs(i, j, visit, picture, m, n);
                if (tmp > max_size_of_one_area){
                    max_size_of_one_area = tmp;
                }
                number_of_area += 1;
            }
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    cout << answer[0];
    cout << answer[1];
    return answer;
}

int main(){
    solution(4, 6, {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}});
    
    return 0;
}
