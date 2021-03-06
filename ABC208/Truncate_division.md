# pythonにおける切り捨て除算について

ABC 208のc問題をpythonで解く時，切り捨て除算を```int()```で行っていたらWCとなった．

pythonの切り捨て除算を```//```の演算子で行うのが定石らしいのでなぜ```int()```ではいけないのかまとめる．

(参考文献:[こちら](https://qiita.com/H20/items/1a066e242815961cd043#2%E9%99%A4%E7%AE%97%E3%81%AE%E5%88%87%E3%82%8A%E4%B8%8A%E3%81%92%E5%88%87%E3%82%8A%E4%B8%8B%E3%81%92
)と[こちら](https://linus-mk.hatenablog.com/entry/2019/05/26/234642
))

## floatとint

今回に限らず，pythonにおいて除算を```a/b```で行ってしまうと型typeがfloatで出るので```int(a/b)```で無理やりにintに直して計算することは可能

```python
#例
print(int(10/3))
```
しかしながら，$10/3$は小数点を用いると無限に$3.33333.....$と続いてしまい計算結果を保持できなくなるので浮動小数点を用いている．

浮動小数点の精度はせいぜい，$\log 2^{53}$みたいなので大体15桁までの計算結果しか精度を保てない.そのために計算結果が16桁以上になると，答えが正しく求まらなくなる.

```python
#答えが変わる例
#今まででやると計算結果が333333333333333312
print(int(1000000000000000000 /3))
#正しい答え 333333333333333333
print(1000000000000000000 //3)
```
## ABC 208
ABC208のC問題は簡単にいうと今持っている$K$個のお菓子を$N$人に均等に分配し，余ったお菓子$K^{\prime}$のお菓子は各人々に割り振られている国民番号$a_i$の小さい順に与えていくという問題であった．
 >詳しくはこちら: [https://atcoder.jp/contests/abc208/tasks/abc208_c](https://atcoder.jp/contests/abc208/tasks/abc208_c)
 この余ったお菓子を求める時に```int(K/N)```を使っていたが，Kが桁数がバカでかい時に配る人数Nがとても小さいと今回の場合は不正解となってしまった．

いい経験になったと思う(レートもかなり下がりました...)

詳しいコードは以下
```python
N, K = map(int, input().split())
a = list(map(int, input().split()))

if K %N == 0:
    for i in range(N):
        print(int(K/N))
else:
    b = sorted(a)
    c = b[K%N]
    for i in range(N):
        if a[i] >= c:
            print(K//N)
        else:
            print(K//N+1)
```
