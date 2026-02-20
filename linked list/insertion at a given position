/*
class Node {
  public:
    int data;
    Node *next;
    Node(int x) {
        data = x;
        next = nullptr;
    }
};
*/

class Solution {
  public:
    Node *insertPos(Node *head, int pos, int val) {
        // code here
        Node* temp=new Node(val);
        
        if (pos==1){
            temp->next=head;
            return temp;
        }
        
        Node* ptr=head;
        for(int i=1;i<pos-1;i++){
            ptr=ptr->next;
        }
        temp->next=ptr->next;
        ptr->next=temp;
        return head;
    }
};
