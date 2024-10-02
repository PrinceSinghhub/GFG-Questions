'''
class Solution {
public:

    void sort(Node** head)

   {
        if (head == nullptr || *head == nullptr) {
            return;
        }


        vector<int> data_vec;
        Node* curr = *head;
        while (curr != nullptr) {
            data_vec.push_back(curr->data);
            curr = curr->next;
        }

        std::sort(data_vec.begin(), data_vec.end());

        curr = *head;
        for (int i = 0; i < data_vec.size(); ++i) {
            curr->data = data_vec[i];
            curr = curr->next;
        }
    }
};
'''