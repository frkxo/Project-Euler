#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define ll long long 
#define arr array
#define pii  pair<int, int>
#define vi vector<int >
#define pb push_back
#define mp make_pair
struct debug {
#ifdef LOCAL
~debug() { cerr << endl; }
eni(!=) cerr << boolalpha << i; ris; }
eni(==) ris << range(begin(i), end(i)); }
sim, class b dor(pair < b, c > d) {
  ris << "(" << d.first << ", " << d.second << ")";
}
sim dor(rge<c> d) {
  *this << "[";
  for (auto it = d.b; it != d.e; ++it)
	*this << ", " + 2 * (it == d.b) << *it;
  ris << "]";
}
#else
sim dor(const c&) { ris; }
#endif
};
#define imie(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "


int main(){
	int n;
	cin >> n;
	int total = 0;
	for(int i = 0;i < n;i++){
		if((i % 3 == 0) || (i % 5 == 0)){
			cout << i << " ";
			total += i;
		}
	}
	cout << "\n" << total;
	return 0;
}
	






