# A. Theatre Square

## 📌 Problem

A rectangular theatre square of size `n × m` meters needs to be covered with square granite flagstones of size `a × a` meters. Flagstones cannot be broken, but they may extend beyond the square. Determine the minimum number of flagstones required.

## 💡 Approach

To cover the square completely:

* Compute the number of flagstones required along the length:

  * `ceil(n / a)`
* Compute the number of flagstones required along the width:

  * `ceil(m / a)`
* Multiply both values to obtain the total number of flagstones.

Since integer arithmetic is used, ceiling division is calculated as:

`(x + a - 1) // a`

## ✅ Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`

## 🛠️ Topics

* Math
* Geometry
* Implementation
* Ceiling Division

## 📚 Key Learning

* Use ceiling division to determine the minimum number of tiles needed to cover a dimension.
* Large input constraints require constant-time mathematical computation instead of simulation.
