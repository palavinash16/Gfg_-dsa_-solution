// traversal of linked list 
/*
class Node {
  public:
    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = NULL;
    }
};
*/

class Solution {
  public:
    void printList(Node* head) {
        // code here
        Node* temp= head;
        
        while(temp!=NULL){
            cout<<temp->data<<" ";
            temp=temp->next;
        }
    }
};
