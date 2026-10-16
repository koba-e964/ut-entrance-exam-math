# [こばのページ](../../../index.html)/[東大入試数学過去問解答例](../../index)/[用語・定理集](../index)/[同値変形について・軌跡や範囲の問題の解き方](./index)

## 定理の言明
変数 $x$ と$x$を含まない式 $A,B$ に対して、$\exists x\ldotp Ax + B = 0$ $\Longleftrightarrow$ $A \neq 0 \lor B = 0$

## 使い方

$\exists x\ldotp Ax+1=0$ を $A \neq 0$ に変形する。

## 証明
$A$ が 0 かどうかで場合わけする。

$A$ が 0 のとき、 

$$\begin{align*}
&\exists x\ldotp Ax + B = 0
\\\\ & \Longleftrightarrow \exists x\ldotp B = 0
\\\\ & \Longleftrightarrow B = 0
\end{align*}$$

$A$ が 0 でないとき、 

$$\begin{align*}
&\exists x\ldotp Ax + B = 0
\\\\ & \Longleftrightarrow \exists x\ldotp x = -\dfrac{B}{A}
\\\\ & \Longleftrightarrow \mathrm{true}
\end{align*}$$

よって、問題の論理式は $(A \neq 0 \land \mathrm{true}) \lor (A = 0 \land B = 0)$ と同値であり、これは $A \neq 0 \lor B = 0$ と同値。
