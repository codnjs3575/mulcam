"""
----------
{1,2,3,4}
{1}{2,3,4}
{1,2}{3,4}
{1,3}{2,4}
{1,4}{2,3}
{1,2,3}{4}
{1,2,4}{3}
{1,3,4}{2}
----------
{1} 고정 후 2,3,4 경우의 수
23, 24, 2, 34, 3, 4
"""
import sys
sys.stdin = open('input.txt','r')

def DFS(arr):
    print(arr[1:])
    new_arr = []
    sum = 0


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    DFS(arr)