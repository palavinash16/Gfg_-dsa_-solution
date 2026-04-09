# 🔗 Linked List (Data Structures)

This folder contains problems and concepts related to Linked Lists in Data Structures.

---

## 📌 What is a Linked List?

A Linked List is a linear data structure where elements (nodes) are stored in memory non-contiguously.  
Each node contains:
- Data
- Pointer to the next node

---

## 🧠 Why Linked List?

- Dynamic size (no fixed size like arrays)
- Efficient insertion and deletion
- Better memory utilization

---

## 🧩 Types of Linked Lists

- Singly Linked List  
- Doubly Linked List  
- Circular Linked List  

---

## 🛠️ Topics Covered

- Linked List Basics  
- Insertion (Beginning, End, Position)  
- Deletion (Beginning, End, Position)  
- Traversal  
- Reverse Linked List  
- Detect Loop *(upcoming)*  
- Find Middle Node *(upcoming)*  

---

## 🔁 Basic Operations

| Operation | Description |
|----------|------------|
| Insert   | Add a node |
| Delete   | Remove a node |
| Traverse | Visit all nodes |
| Search   | Find a node |

---

## 📂 Problems

| Problem | Difficulty | Status |
|--------|------------|--------|
| Insert at Beginning | Easy | 🔄 |
| Insert at End | Easy | 🔄 |
| Delete Node | Easy | 🔄 |
| Reverse Linked List | Easy | 🔄 |
| Detect Loop | Medium | ⏳ |

---

## 🧱 Structure of Node (C++)

```cpp
struct Node {
    int data;
    Node* next;
};
