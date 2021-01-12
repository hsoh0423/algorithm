#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	long long num, meter;
	scanf_s("%lld%lld", &num, &meter);

	long long trees[1000000];

	long long max = 0;
	for (long long i = 0; i < num; i++)
	{
		scanf_s("%lld", &trees[i]);
		if (trees[i] > max)
		{
			max = trees[i];
		}
	}
		
	long long start = 0;
	long long end = max;
	long long n;
	long long sum = 0;
	long long mid = (start + end) / 2;
	while (end > start)
	{
		sum = 0;
		mid = (start + end) / 2;

		for (long long i = 0; i < num; i++)
		{
			n = trees[i] - mid;
			if (n > 0)
			{
				sum += n;
			}
		}
		if (sum == meter || start == mid || end == mid)
		{
			printf("%lld", mid);
			break;
		}
		else if(sum > meter)
		{
			start = mid;
		}
		else if (sum < meter)
		{
			end = mid ;
		}
	}
}