"""
Description:
Satish wants to prepare for tommorow's exam . He knows the distribution of marks for the subject along with time to
learn the concepts.You are given remaining time for the exam along with marks for each topic and passing marks for
the subject.Find the max marks Satish can attain by studing max no of topic in max no hours not excedding (p) .


Input: The first line of input contains the number of testcases t.The first line of each testcase contains the no of
topics(n) , time remaining for exam(h) in hour and passing marks(p).Each 'n' lines contain u(time to learn topic) and
v(weightage of topic in exam) .
1
5 40 21
12 10
16 10
20 10
24 10
8 3

Output:
For each test case print "YES" along with time taken or "NO".
Constraints:
1<=t<=100
1<=n<=300
1<=h<=150
1<=p<=35
1<=u,v<=25
YES 36
"""

"""
#include <iostream>
#include <vector>
using namespace std;
int main() {
	int t; cin >>t;
	while(t--){
	    int n , H , P;
	    cin >> n >> H >> P ; vector<int>tim(n) ; vector<int>val(n);
	    for(int i =0; i <n; i ++){
	        cin >> tim[i];
	        cin >> val[i];
	    }
	    int dp[n+1][H+1];
	    for(int i = 0; i <=n; i ++){
	        for(int j =0; j <= H; j++){
	            if(i==0 || j == 0)  dp[i][j] = 0;
	            else if(tim[i-1] <= j){dp[i][j] = max(val[i-1]+dp[i-1][j-tim[i-1]], dp[i-1][j]);}
	            else dp[i][j] = dp[i-1][j];
	        }
	    }

	   if(dp[n][H] < P) cout << "NO" <<endl;
	   else{
	       int sum =  dp[n][H];int res = 0;int t = H;
	       for(int i = n; i>0 && t>0; i--){
	           if(sum == dp[i-1][t])continue;
	           else{
	               res+= tim[i-1];
	               t = t- tim[i-1];
	               sum = sum - val[i-1];
	           }
	       }
	       cout << "YES" << " " << res <<endl;
	   }
	}
	return 0;
}
"""
