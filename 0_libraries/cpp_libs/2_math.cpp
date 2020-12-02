#include "xx_def.hpp"

long long pow_mod(long long x, long long n, long long mod){
    if(n == 0) { return 1; }
    ll xx = x;
    ll nn = n;
    ll k = 1;
    while(nn > 1){
        if(nn%2 != 0){ k *= xx; }
        xx *= xx;
        nn = nn/2;
        xx%=mod;
    }
    return k * xx;
}


ll lcm(ll a, ll b){ return (a / __gcd(a,b)) * b; }


vector<ll> divs(ll n){
    vector<ll> divs;
    for(ll i = 1 ; i*i <= n ; i++){
        if(n%i == 0){
            divs.push_back(i);
            if(i*i != n){
                divs.push_back(n/i);
            }
        }
    }
    sort(divs.begin(), divs.end());
    return divs;
}


vector<ll> primes(ll n){
    vector<bool> is_prime(n+1, true);
    is_prime[0] = false;
    is_prime[1] = false;
    for(ll i = 2 ; i*i <= n ; i++){
        if(is_prime[i]){
            for(ll j = i*2 ; j <= n ; j+=i){
                is_prime[j] = false;
            }
        }
    }
    vector<ll> ps;
    for(ll i = 2 ; i <= n ; i++){
        if(is_prime[i]) ps.push_back(i);
    }
    return ps;
}


vector<P> p_factorization(ll n){
    vector<P> facs;
    if(n == 1) return facs;
    ll curr_n = n;
    for(ll i = 2 ; i*i <= n ; i++){
        if(curr_n%i == 0){
            ll cnt = 0;
            while(curr_n%i == 0){
                cnt += 1;
                curr_n /= i;
            }
            facs.push_back(P(i,cnt));
        }
    }
    if(curr_n != 1) facs.push_back(P(curr_n,1));
    return facs;
}


map<ll,ll> p_factorization_m(ll n){
    map<ll,ll> facs;
    if(n == 1) return facs;
    ll curr_n = n;
    for(ll i = 2 ; i*i <= n ; i++){
        if(curr_n%i == 0){
            ll cnt = 0;
            while(curr_n%i == 0){
                cnt += 1;
                curr_n /= i;
            }
            facs[i] = cnt;
        }
    }
    if(curr_n != 1) facs[curr_n] = 1;
    return facs;
}

unordered_map<ll,ll> p_factorization_m2(ll n){
    unordered_map<ll,ll> facs;
    if(n == 1) return facs;
    ll curr_n = n;
    for(ll i = 2 ; i*i <= n ; i++){
        if(curr_n%i == 0){
            ll cnt = 0;
            while(curr_n%i == 0){
                cnt += 1;
                curr_n /= i;
            }
            facs[i] = cnt;
        }
    }
    if(curr_n != 1) facs[curr_n] = 1;
    return facs;
}


int main(){
    cout << pow_mod(3,4,5) << endl;
    cout << lcm(4,6) << endl;
    DEBUGL(divs(40));
    DEBUGL(primes(50));
    DEBUGLP(p_factorization(12));
    DEBUGM(p_factorization_m(12));
}

