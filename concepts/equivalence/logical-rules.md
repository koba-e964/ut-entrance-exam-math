# [こばのページ](../../../index.html)/[東大入試数学過去問解答例](../../index)/[用語・定理集](../index)/[同値変形について・軌跡や範囲の問題の解き方](./index)

## 論理式の規則

$P,Q,R$ は命題，変数は全て実数をとるものとする。

- 分配法則
  - $P \land (Q \lor R)$ $\Longleftrightarrow$ $(P \land Q) \lor (P \land R)$
  - $P \lor (Q \land R)$ $\Longleftrightarrow$ $(P \lor Q) \land (P \lor R)$
- 否定の変形
  - $\neg(P \land Q)$ $\Longleftrightarrow$ $\neg P \lor \neg Q$
  - $\neg(P \lor Q)$ $\Longleftrightarrow$ $\neg P \land \neg Q$
  - $\neg(\forall x\ldotp P)$ $\Longleftrightarrow$ $\exists x\ldotp \neg P$
  - $\neg(\exists x\ldotp P)$ $\Longleftrightarrow$ $\forall x\ldotp \neg P$
- 含意の変形
  - $(P \Rightarrow Q)$ $\Longleftrightarrow$ $\neg P \lor Q$
- 量化記号の分配
  - $\exists x\ldotp (P \lor Q)$ $\Longleftrightarrow$ $(\exists x\ldotp P) \lor (\exists x\ldotp Q)$
  - $\forall x\ldotp (P \land Q)$ $\Longleftrightarrow$ $(\forall x\ldotp P) \land (\forall x\ldotp Q)$
  - $\exists$ は $\land$ に，$\forall$ は $\lor$ に一般には分配できない。

変数に依存しない条件は，量化記号の外に出せる。例えば，

- $\exists x\ldotp (x^2=1 \land y>0)$
  - $\Longleftrightarrow$ $(\exists x\ldotp x^2=1) \land y>0$
  - $\Longleftrightarrow$ $y>0$

一般に，$Q$ に $x$ が自由変数として含まれない場合，

- $\exists x\ldotp (P \land Q)$ $\Longleftrightarrow$ $(\exists x\ldotp P) \land Q$
- $\exists x\ldotp Q$ $\Longleftrightarrow$ $Q$
