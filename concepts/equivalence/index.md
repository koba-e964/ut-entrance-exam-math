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

全てのタクティックについて、左側と右側が同値で、左側より右側が単純になっていることを確認されたい。

- 方程式の求解
  - 因数分解をする。
  - 例: $x^2 - 5x = -6$ $\Longleftrightarrow$ $(x-2)(x-3) = 0$
    - $\Longleftrightarrow$ $x-2 = 0 \lor x-3 = 0$
    - $\Longleftrightarrow$ $x=2 \lor x=3$
- 代入法
  - $x = A \land P$ $\Longleftrightarrow$ $x = A \land P\mid _ {x=A}$
  - 例: $y = 2x + 1 \land x^2 + y^2 = 1$ $\Longleftrightarrow$ $y = 2x+1 \land x^2 + (2x+1)^2 = 1$
    - $\Longleftrightarrow$ $y = 2x+1 \land x(5x+4)=0$ (方程式の求解)
    - $\Longleftrightarrow$ $y = 2x+1 \land (x=0 \lor x = -\dfrac{4}{5})$ (方程式の求解)
    - $\Longleftrightarrow$ $(y = 2x+1 \land x=0) \lor (y = 2x+1 \land x = -\dfrac{4}{5})$ (分配法則)
    - $\Longleftrightarrow$ $(y = 1 \land x=0) \lor (y = -\dfrac{3}{5} \land x = -\dfrac{4}{5})$ (代入)
- 束縛変数の消滅
  - $P$ に 変数 $x$ が含まれない場合、$\exists x\ldotp P$ $\Longleftrightarrow$ $P$
- 束縛範囲の縮小
  - $Q$ に 変数 $x$ が含まれない場合、$\exists x\ldotp P \land Q$ $\Longleftrightarrow$ $(\exists x\ldotp P) \land Q$
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
