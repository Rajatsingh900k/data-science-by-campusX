Here’s a detailed explanation for each question related to **Python memory management and data behavior** 👇

---

### **1. What is aliasing?**

Aliasing occurs when **two or more variables refer to the same object in memory**.
Changing the object through one variable affects the other, since both point to the same reference.

```python
a = [1, 2, 3]
b = a        # aliasing
b.append(4)
print(a)     # [1, 2, 3, 4]
```

✅ `a` and `b` are aliases for the same list object.

---

### **2. What is garbage collection?**

Garbage collection is the process by which **Python automatically frees memory** by deleting objects that are **no longer referenced**.
Python uses **reference counting** and a **cyclic garbage collector** to manage memory.

```python
import gc
gc.collect()  # Manually trigger garbage collection
```

✅ When an object’s reference count drops to 0, it becomes eligible for garbage collection.

---

### **3. What is mutability and why is it dangerous in certain scenarios?**

* **Mutability** means an object’s value **can be changed** after creation (e.g., `list`, `dict`, `set`).
* **Immutable** objects (like `int`, `str`, `tuple`) cannot be changed in place.

Danger: Mutability can cause **unexpected side effects** when multiple variables reference the same object.

```python
x = [1, 2, 3]
y = x
y[0] = 100
print(x)  # [100, 2, 3]
```

⚠️ Both `x` and `y` changed because they reference the same mutable list.

---

### **4. What is cloning?**

Cloning means **creating a copy of an object**.
It can be done using:

* **Shallow copy** → `copy.copy(obj)`
* **Deep copy** → `copy.deepcopy(obj)`

```python
import copy
a = [1, 2, [3, 4]]
b = copy.copy(a)       # Shallow copy
c = copy.deepcopy(a)   # Deep copy
```

---

### **5. Differentiate between deep and shallow copies**

| Type             | Definition                                            | Example           | Effect                      |
| ---------------- | ----------------------------------------------------- | ----------------- | --------------------------- |
| **Shallow Copy** | Copies only outer object; inner references are shared | `copy.copy()`     | Inner objects remain linked |
| **Deep Copy**    | Recursively copies all objects                        | `copy.deepcopy()` | Fully independent copy      |

```python
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)       # shallow
c = copy.deepcopy(a)   # deep

a[0][0] = 99
print(b)  # [[99, 2], [3, 4]]
print(c)  # [[1, 2], [3, 4]]
```

---

### **6. How nested lists are stored in memory?**

Nested lists are stored as **references to other list objects**.
Each inner list has its **own memory address**, and the outer list stores **references** (pointers) to them.

```python
a = [[1, 2], [3, 4]]
print(id(a), id(a[0]), id(a[1]))
```

✅ The outer list only holds memory addresses of the inner lists.

---

### **7. How strings are stored in memory?**

Strings in Python are **immutable** and stored as **objects in a memory pool** (string interning for small or frequently used strings).
Every time you modify a string, **a new string object** is created.

```python
a = "hello"
b = a
a += " world"
print(a, b)  # 'hello world', 'hello'
```

✅ `a` points to a new object, while `b` still points to the old one.

---

### **8. Why tuples take less memory than lists?**

* Tuples are **immutable**, so Python can **optimize storage** and **avoid extra overhead** for resizing.
* Lists keep **extra buffer space** for future element additions.

```python
import sys
print(sys.getsizeof([1, 2, 3]))   # Larger
print(sys.getsizeof((1, 2, 3)))   # Smaller
```

---

### **9. How set index position is decided?**

Sets are **unordered** collections — they use **hashing**.
The position of each element in memory is based on its **hash value**, which determines where it’s stored in the underlying **hash table**.

```python
s = {10, 20, 30}
print(hash(10))
```

✅ That’s why set elements don’t maintain any particular order.

---

### **10. Why mutable types are not allowed in sets/dicts?**

Because sets and dicts rely on **hash values** for element lookups.
If an object is mutable, its value (and hence its hash) can change, which would **break the integrity** of the hash table.

```python
s = {[1, 2]}  # ❌ TypeError: unhashable type: 'list'
```

✅ Immutable objects like `tuple` or `str` are hashable and can be used as keys or set elements.

---

Would you like me to make this into a **formatted PDF or Markdown file** for download?
