/*
Problem: Inorder Traversal
Topic: Trees
Difficulty: Easy

Approach:
- Use recursion
- Traverse Left → Root → Right

Time Complexity: O(n)
Space Complexity: O(h)
*/

#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

void inorder(Node* root) {
    if (root == NULL) return;

    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}
