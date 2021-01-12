#include <iostream>
#include <queue>
#include <vector>

using namespace std;

char c;
bool visit[100][100];

void bfs(char arr[][100], int row, int col, bool visit[][100], char c, int num)
{
	queue<pair<int, int>> q;
	q.push(pair<int, int>(row, col));
	while (!q.empty())
	{
		row = q.front().first;
		col = q.front().second;
		q.pop();
		if (row > num - 1 || col > num - 1 || row < 0 || col < 0)
		{
			continue;
		}
		if (arr[row][col] == c && visit[row][col] == false)
		{
			q.push(pair<int, int>(row, col + 1));
			q.push(pair<int, int>(row + 1, col));
			q.push(pair<int, int>(row, col - 1));
			q.push(pair<int, int>(row - 1, col));
			visit[row][col] = true;
			cout << row << col << endl;
		}
	}
}

int search(char arr[][100], int num)
{
	c = arr[0][0];
	int count = 0;
	for (int i = 0; i < 100; i++)
	{
		for (int j = 0; j < 100; j++)
		{
			visit[i][j] = false;
		}
	}

	for (int i = 0; i < num; i++)
	{
		for (int j = 0; j < num; j++)
		{
			if (visit[i][j] == true)
			{
				continue;
			}
			else
			{
				//cout << i << j << endl;
				c = arr[i][j];
				bfs(arr, i, j, visit, c, num);
				count++;
			}
		}
	}
	return count;
}
int main()
{
	int num;
	scanf_s("%d", &num);

	char arr[100][100];

	for (int i = 0; i < num; i++)
	{
		for (int j = 0; j < num; j++)
		{
			scanf_s(" %c", &arr[i][j], 1);
		}
	}

	int result = search(arr, num);
	printf("%d ", result);

	for (int i = 0; i < num; i++)
	{
		for (int j = 0; j < num; j++)
		{
			if (arr[i][j] == 'R')
			{
				arr[i][j] = 'G';
			}
		}
	}
	result = search(arr, num);
	printf("%d", result);
}