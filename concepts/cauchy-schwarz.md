# コーシー・シュヴァルツの不等式

## 定理の言明

任意の実数$a,b,x,y$に対して、

$$(a^2 + b^2)(x^2+y^2) \ge (ax+by)^2 \tag{1}$$

が成り立つ。この不等式において、等号が成り立つことと、$ay = bx$ は同値である。


また、6変数以上の時も同様で、任意の正の整数 $n$ と任意の実数 $a_1, \ldots, a_n, b_1,\ldots, b _ n$ に対し，

$$\left(\sum_{1 \le i \le n} a_i^2\right) \left(\sum_{1 \le i \le n} b_i^2\right) \ge \left(\sum_{1 \le i \le n} a_ib_i\right)^2 \tag{2}$$

が成り立つ。また、別の表し方としてベクトルを使うと、

$$\left|\begin{pmatrix} a _ 1 \\ a _ 2 \\ \vdots \end{pmatrix}\right|^2\left|\begin{pmatrix} b _ 1 \\ b _ 2 \\ \vdots \end{pmatrix}\right|^2 \ge \left(\begin{pmatrix} a _ 1 \\ a _ 2 \\ \vdots \end{pmatrix} \cdot \begin{pmatrix} b _ 1 \\ b _ 2 \\ \vdots \end{pmatrix} \right)^2$$

と表すこともできる。

この不等式において、等号が成り立つことと、ある実数 $(s, t) \neq (0, 0)$ が存在して任意の $i$ に対して $sa_i = tb_i$ であることは同値である。

## 使い方

$x + 4y = 6$ のとき、 $(1^2 + 4^2)(x^2 + y^2) \ge (x + 4y)^2 = 36$ であるため、 $x^2 + y^2 \ge \dfrac{36}{17}$ である。等号成立は $4x = y$ と、つまり $(x, y) = \left(\dfrac{6}{17}, \dfrac{24}{17}\right)$ と同値である。

よって、$x^2 + y^2$ の最小値は $\dfrac{36}{17}$ である。

## 証明

$$\left(\sum_{1 \le i \le n} a_i^2\right) \left(\sum_{1 \le i \le n} b_i^2\right) \ge \left(\sum_{1 \le i \le n} a_ib_i\right)^2$$

の方を証明する。 $x$ の (高々) 2次の式 $T(x) = \sum_{1 \le i \le n} (a_ix - b_i)^2$ を考えよう。

### (i) 符号
常に $T(x) \ge 0$ である。これは常に $(a_ix - b_i)^2 \ge 0$ が成立することから明らか。

### (ii) 判別式
$T(x)$ を展開すると

$$T(x) = \left(\sum_{1 \le i \le n} a_i^2\right)x^2 - 2\left(\sum_{1 \le i \le n} a_ib_i\right) x + \sum_{1 \le i \le n} b_i^2$$

である。 $\sum_{1 \le i \le n} a_i^2 \ne 0$ であれば、これは2次式であり、判別式を4で割ったものは

$$\left(\sum_{1 \le i \le n} a_ib_i\right)^2 - \left(\sum_{1 \le i \le n} a_i^2\right) \left(\sum_{1 \le i \le n} b_i^2\right)$$

である。
### まとめ
(i)(ii) から、$\sum_{1 \le i \le n} a_i^2 \ne 0$ である場合は判別式が 0 以下であることがわかる。つまり

$$\left(\sum_{1 \le i \le n} a_i^2\right) \left(\sum_{1 \le i \le n} b_i^2\right) \ge \left(\sum_{1 \le i \le n} a_ib_i\right)^2$$

が成り立つ。等号が成り立つことと判別式が 0 であることは同値であり、これはすべての $i$ に対して $a_ix - b_i = 0$ となる $x$ が存在することと同値。ある実数 $(s, t) \neq (0, 0)$ が存在して任意の $i$ に対して $sa_i = tb_i$ であることとも同値である。

- ($\Rightarrow$): $s = x, t = 1$ とすればよい。
- ($\Leftarrow$): $t \ne 0$ であれば $x = \dfrac{s}{t}$ とすればよい。 $t = 0$ であれば $s \ne 0$ であるが、このとき $a_i = 0$ となり、$\sum_{1 \le i \le n} a_i^2 \ne 0$ と矛盾する。

$\sum_{1 \le i \le n} a_i^2 = 0$ のとき、すべての $i$ に対して $a_i = 0$ である。 このとき (2) は $0 = 0$ となり自明。 $a_i = 0$ だから $(s, t) = (1, 0)$ とすれば $sa_i = tb_i$ も常に成り立つ。

Qed.

## 注意

- 正の実数などには限定されない。
- 「コーシー・シュワルツの不等式」と表記されることもある。この定理の名前の元となった [Karl Hermann Amandus Schwarz](https://ja.wikipedia.org/wiki/%E3%83%98%E3%83%AB%E3%83%9E%E3%83%B3%E3%83%BB%E3%82%A2%E3%83%9E%E3%83%B3%E3%83%89%E3%82%A5%E3%82%B9%E3%83%BB%E3%82%B7%E3%83%A5%E3%83%B4%E3%82%A1%E3%83%AB%E3%83%84) はドイツの数学者であり、ドイツ語では `w` の文字は `/v/` と発音される。
- 積分形もある。内積に見えるものがあれば適用できる。
- 複素数の場合も、適切に内積を定義すれば成り立つ。
