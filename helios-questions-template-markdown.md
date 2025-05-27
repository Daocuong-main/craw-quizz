# Xem đoạn code sau
```typescript
interface User {
  id: number;
  name: string;
  age?: number;
}
const getUserInfo = (user: User): string => {
  return `ID: ${user.id}, Name: ${user.name}, Age: ${user.age ?? "N/A"}`;
};
console.log(getUserInfo({ id: 1, name: "Alice" }));
console.log(getUserInfo({ id: 2, name: "Bob", age: 25 }));
```

* ```
  ID: 1, Name: Alice, Age: N/A
  ID: 2, Name: Bob, Age: 25
  ```

- ```txt
  ID: 1, Name: Alice, Age: undefined
  ID: 2, Name: Bob, Age: 25
  ```

- ```txt
  ID: 1, Name: Alice
  ID: 2, Name: Bob, Age: 25
  ```

- ```txt
  Error: Property 'age' is missing in type '{ id: number; name: string; }' but required in type 'User'.
  ```

# Kết quả của đoạn code sau trong JavaScript là gì?
```javascript
console.log(1 + "1" - 1)
```

- "11"
- "10"
* 10
- NaN

# Trong TypeScript, cách khai báo mảng nào là đúng?

- ```typescript

 let arr: Array = [1, 2, 3];```
- ```typescript

 let arr: number[] = [1, 2, 3];```

- ```typescript

 let arr = <number[]> [1, 2, 3];```

- ```typescript

 let arr: numbers = [1, 2, 3];```

# Giá trị của `x` sau khi chạy đoạn code sau là gì?

```javascript
    let x = 0;
    x ||= 5;
    console.log(x);
```

- 0
* 5
- undefined
- NaN

# Trong TypeScript, kiểu dữ liệu nào dưới đây là không hợp lệ?

- string
- boolean
* anyobject
- number

# Kết quả của đoạn code sau trong Python là gì?

```python
def test(a, b=[]):
        b.append(a)
        return b

    print(test(1))
    print(test(2))
```

- [1] [2]
- [1] [1, 2]
* [1] [1, 2]
- [1] [2]

# Kết quả của đoạn code sau trong JavaScript là gì?

```javascript
console.log(typeof NaN);
```

- string
- number
- *"number"*
- undefined

# Để import toàn bộ module trong Node.js, câu lệnh nào đúng?

- ```import * from 'fs';```
- ```require('fs')```
* ```import * as fs from 'fs';```
- ```import fs from 'fs';```

# Kết quả của đoạn code sau trong Python là gì?

```python
x = (1, 2, 3)
    x[0] = 10
```

- ```(10, 2, 3)```
* ```TypeError```
- ```(1, 2, 3)```
- ```None```

# Kết quả của đoạn code sau trong JavaScript là gì?

```javascript
 console.log(0 == "0");
    console.log(0 === "0");
```

- true true
- false false
* true false
- false true
