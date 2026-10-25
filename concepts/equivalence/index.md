# [こばのページ](../../../index.html)/[東大入試数学過去問解答例](../../index)/[用語・定理集](../index)/同値変形について・軌跡や範囲の問題の解き方

方程式を解く、軌跡や範囲を求めるというのは、数学の言葉で言うと、

- **同値**であって、より単純な論理式を求めよ

というのと同じである。

### 同値変形のタクティック一覧

以下、このような記号を使う。

- 変数: $x, y, s, t, \ldots$
- 式: $A, B, C, \ldots$
- 命題: $P, Q, \ldots$

また、暗黙のうちに全ての変数は実数をとるものとする。

### 1. 条件を整理する

分配法則などで，場合ごとに処理できる形にする。

- 例: $y=2x+1 \land (x=0 \lor x=1)$
  - $\Longleftrightarrow$ $(y=2x+1 \land x=0) \lor (y=2x+1 \land x=1)$
  - $\Longleftrightarrow$ $(y=1 \land x=0) \lor (y=3 \land x=1)$

否定・含意・量化記号などの規則は，[論理式の規則](./logical-rules)を参照。

### 2. 等式で変数を消す

$x=A$ があれば代入する。以下，$A$ は $x$ を含まない式とする。

- $x=A \land P$ $\Longleftrightarrow$ $x=A \land P\mid _ {x=A}$
- $\exists x\ldotp (x=A \land P)$ $\Longleftrightarrow$ $P\mid _ {x=A}$

例えば，$\exists x\ldotp (y=2x+1 \land x=0)$ $\Longleftrightarrow$ $y=1$。
代入すると $x$ が残らないので，$\exists x$ も消える。

方程式を因数分解して，代入できる形にすることもある。

- 例: $x^2-5x=-6$ $\Longleftrightarrow$ $(x-2)(x-3)=0$ $\Longleftrightarrow$ $x=2 \lor x=3$

### 3. 変数が存在する条件に直す

区間・方程式の根・関数の値域を使って，$\exists$ を消す。

- 区間が空でない条件
  - $x$ を含まない式 $A,B$ に対して，$\exists x\ldotp (A \le x \land x \le B)$ $\Longleftrightarrow$ $A \le B$
  - 左辺の不等号が片方でも狭義なら，右辺も $A < B$ となる。
- 1変数のグラフ的解析
  - $\exists x\ldotp x \in I \land A = f(x)$ $\Longleftrightarrow$ $A \in (fのIにおける値域)$ (増減などを調べて値域を求める)
  - 例: $\exists x\ldotp x \ge 0 \land y = x^2 - x$ $\Longleftrightarrow$ $y \in [-1/4, \infty)$ $\Longleftrightarrow$ $y \geq -\dfrac{1}{4}$
- 変数の置き換え
  - $\exists x\ldotp P \mid _ {u = A}$ $\Longleftrightarrow$ $\exists u\ldotp P \land (\exists x\ldotp u = A)$
  - 例: $\exists x\ldotp x^4 + x^2 = k$ $\Longleftrightarrow$ $\exists u\ldotp u^2 + u = k \land (\exists x\ldotp u = x^2)$
    - $\Longleftrightarrow$ $\exists u\ldotp u^2 + u = k \land u \ge 0$ ($x^2$に対する1変数のグラフ的解析)
    - $\Longleftrightarrow$ $k \ge 0$ ($u^2+u$に対する1変数のグラフ的解析)
- [1次方程式の実数根の存在](./linear-real-roots)
  - $x$を含まない式 $A,B$ に対して、$\exists x\ldotp Ax + B = 0$ $\Longleftrightarrow$ $A \neq 0 \lor B = 0$
- [2次方程式の実数根の存在](./quadratic-real-roots)
  - $x$を含まない式 $A,B,C$ に対して、$A \neq 0 \land \exists x\ldotp Ax^2 + Bx + C = 0$ $\Longleftrightarrow$ $A \neq 0 \land B^2 \ge 4AC$
- [根と係数の関係](./vieta)
  - $\exists s\ldotp \exists t\ldotp A = s + t \land B = st$ $\Longleftrightarrow$ $A^2 \ge 4B$
