# 🧱 Stack (Data Structures)

This folder contains problems and concepts related to Stack in Data Structures.

---

## 📌 What is a Stack?

A Stack is a linear data structure that follows the **LIFO (Last In First Out)** principle.

👉 The last element inserted is the first one to be removed.

---

## 🧠 Why Stack?

- Used in recursion  
- Expression evaluation (infix, postfix, prefix)  
- Undo/Redo operations  
- Backtracking problems  

---

## 🛠️ Operations in Stack

| Operation | Description |
|----------|------------|
| Push     | Insert element |
| Pop      | Remove top element |
| Top/Peek | Get top element |
| isEmpty  | Check if stack is empty |

---


🛠️ Topics Covered
Stack Basics
Implementation using Array
Implementation using Linked List
Reverse a Stack (upcoming)
Next Greater Element (upcoming)

📂 Problems

Problem	Difficulty	Status
Implement Stack	Easy	🔄Valid Parentheses	Easy	🔄Reverse Stack	Medium	⏳Next Greater Element	Medium	⏳


🧱 Stack Implementation (C++)

#include <stack>
using namespace std;

int main() {
    stack<int> st;
    st.push(10);
    st.push(20);
    st.pop();
    return 0;
}

🎯 Goals

Master stack operations
Solve expression-based problems
Improve problem-solving speed

📎 Notes

Stack follows LIFO
Very important for interviews
Often used with recursion



