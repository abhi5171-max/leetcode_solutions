# B. Burglar and Matches

## 📌 Problem Statement

A burglar breaks into a warehouse containing **m containers**. Each container has:

- `ai` matchboxes
- `bi` matches in each matchbox

The burglar's bag can carry **exactly `n` matchboxes**. The objective is to maximize the total number of matches stolen.

---

## 💡 Approach

This problem is a classic **Greedy Algorithm**.

Since every matchbox occupies the same amount of space, the optimal strategy is to always pick matchboxes from the container with the **highest number of matches per matchbox** first.

### Steps:
1. Store each container as `(matchboxes, matchesPerBox)`.
2. Sort all containers in **descending order** of `matchesPerBox`.
3. Traverse the sorted list:
   - Take as many matchboxes as possible from the current container.
   - Update the remaining capacity.
   - Stop when the bag is full.
4. Output the total number of matches collected.

This greedy choice guarantees the maximum possible number of matches.

---

## 🚀 Algorithm

1. Read `n` and `m`.
2. Store all containers.
3. Sort containers by matches per box in descending order.
4. For each container:
   - Take `min(remainingCapacity, availableBoxes)`.
   - Add `taken × matchesPerBox` to the answer.
   - Reduce remaining capacity.
5. Print the total matches.

---

## ✅ Java Solution

```java
import java.util.*;

public class Main {
    static class Container {
        int boxes, matches;

        Container(int boxes, int matches) {
            this.boxes = boxes;
            this.matches = matches;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        Container[] containers = new Container[m];

        for (int i = 0; i < m; i++) {
            containers[i] = new Container(sc.nextInt(), sc.nextInt());
        }

        Arrays.sort(containers, (a, b) -> b.matches - a.matches);

        int totalMatches = 0;
        int remaining = n;

        for (Container c : containers) {
            if (remaining == 0)
                break;

            int take = Math.min(remaining, c.boxes);
            totalMatches += take * c.matches;
            remaining -= take;
        }

        System.out.println(totalMatches);
    }
}
```

---

## ⏱️ Time Complexity

- **Sorting:** `O(m log m)`
- **Traversal:** `O(m)`

**Overall:** `O(m log m)`

---

## 💾 Space Complexity

- **O(m)** (to store the containers)

---

## 🧪 Example

### Input

```
7 3
5 10
2 5
4 7
```

### Output

```
64
```

### Explanation

After sorting by matches per box:

| Matchboxes | Matches/Box |
|------------|-------------|
| 5 | 10 |
| 4 | 7 |
| 2 | 5 |

- Take all **5** boxes from the first container → `5 × 10 = 50`
- Remaining capacity = **2**
- Take **2** boxes from the second container → `2 × 7 = 14`

Total matches = **50 + 14 = 64**

---

## 🎯 Key Takeaways

- Greedy algorithms work when making the locally optimal choice leads to the globally optimal solution.
- Sorting based on the value per unit (matches per box) is the key observation.
- Efficient implementation using sorting ensures the optimal answer within the given constraints.

---

## 🏷️ Tags

`Greedy` `Sorting` `Implementation` `Codeforces`