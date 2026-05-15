#include <iostream>
#include <cctype>
using namespace std;

struct node {
    node* prev;
    int id;
    string name;
    string department;
    node* next;
};

node* head = NULL;
int count = 0;

//********************** COUNT NODES **********************
void num() {
    if (head == NULL) {
        count = 0;
        return;
    }

    node* ptr = head;
    count = 0;
    do {
        count++;
        ptr = ptr->next;
    } while (ptr != head);
}

//********************** CHECK DUPLICATE ID **********************
bool isDuplicateID(int id) {
    if (head == NULL) {
        return false;
    }
    
    node* ptr = head;
    do {
        if (ptr->id == id) {
            return true;
        }
        ptr = ptr->next;
    } while (ptr != head);
    
    return false;
}

//********************** VALIDATE NAME (NO NUMBERS ALLOWED) **********************
bool isValidName(string name) {
    if (name.empty()) {
        return false;
    }
    
    for (int i = 0; i < name.length(); i++) {
        if (isdigit(name[i])) {
            return false;
        }
    }
    return true;
}

//********************** ADD AT BEGINNING **********************
void add_at_beg(int id, string name, string department) {
    if (isDuplicateID(id)) {
        cout << "\n!!! Error: ID " << id << " already exists! Cannot add duplicate ID. !!!" << endl;
        return;
    }
    
    if (!isValidName(name)) {
        cout << "\n!!! Error: Name cannot contain numbers or be empty! !!!" << endl;
        return;
    }
    
    node* ptr = new node;
    ptr->id = id;
    ptr->name = name;
    ptr->department = department;

    if (head == NULL) {
        head = ptr;
        ptr->prev = ptr;
        ptr->next = ptr;
        return;
    }

    node* x = head->prev;
    ptr->next = head;
    ptr->prev = x;
    x->next = ptr;
    head->prev = ptr;
    head = ptr;
}

//********************** ADD AT END **********************
void add_at_end(int id, string name, string department) {
    if (isDuplicateID(id)) {
        cout << "\n!!! Error: ID " << id << " already exists! Cannot add duplicate ID. !!!" << endl;
        return;
    }
    
    if (!isValidName(name)) {
        cout << "\n!!! Error: Name cannot contain numbers or be empty! !!!" << endl;
        return;
    }
    
    node* ptr = new node;
    ptr->id = id;
    ptr->name = name;
    ptr->department = department;

    if (head == NULL) {
        head = ptr;
        ptr->prev = ptr;
        ptr->next = ptr;
        return;
    }

    node* x = head->prev;
    x->next = ptr;
    ptr->prev = x;
    ptr->next = head;
    head->prev = ptr;
}
//********************** ADD AT POSITION **********************
void add_at_pos(int id, string name, string department, int place) {
    if (isDuplicateID(id)) {
        cout << "\n!!! Error: ID " << id << " already exists! Cannot add duplicate ID. !!!" << endl;
        return;
    }
    
    if (!isValidName(name)) {
        cout << "\n!!! Error: Name cannot contain numbers or be empty! !!!" << endl;
        return;
    }
    
    num();
    if (place > count + 1  place <= 0) {
        cout << "\n!!! Invalid position or out of range !!!" << endl;
        return;
    }

    node* ptr = new node;
    ptr->id = id;
    ptr->name = name;
    ptr->department = department;

    if (head == NULL) {
        head = ptr;
        ptr->prev = ptr;
        ptr->next = ptr;
        return;
    }

    if (place == 1) {
        add_at_beg(id, name, department);
        return;
    }

    node* x = head;
    for (int i = 1; i < place - 1; i++) {
        x = x->next;
    }
    ptr->prev = x;
    ptr->next = x->next;
    x->next = ptr;
    ptr->next->prev = ptr;
}

//********************** DISPLAY **********************
void display() {
    if (head == NULL) {
        cout << "\n=== The list is empty ===" << endl;
        return;
    }

    num();
    cout << "\n======= DOUBLY CIRCULAR LINKED LIST =======" << endl;
    cout << "Total nodes: " << count << endl;
    cout << "-------------------------------------------" << endl;
    cout << "ID\tName\t\tDepartment" << endl;
    cout << "-------------------------------------------" << endl;

    node* ptr = head;
    do {
        cout << ptr->id << "\t" << ptr->name << "\t\t" << ptr->department << endl;
        ptr = ptr->next;
    } while (ptr != head);
    cout << "===========================================\n" << endl;
}

//********************** DELETE AT BEGINNING **********************
void del_at_beg() {
    if (head == NULL) {
        cout << "\n!!! Nothing to delete - List is empty !!!" << endl;
        return;
    }

    if (head->next == head) {
        cout << "\n=== Deleted node with ID: " << head->id << " from beginning ===" << endl;
        delete head;
        head = NULL;
        return;
    }

    node* ptr = head->prev;
    node* x = head;
    cout << "\n=== Deleted node with ID: " << head->id << " from beginning ===" << endl;
    head = head->next;
    ptr->next = head;
    head->prev = ptr;
    delete x;
}

//********************** DELETE AT END **********************
void del_at_end() {
    if (head == NULL) {
        cout << "\n!!! Nothing to delete - List is empty !!!" << endl;
        return;
    }

    if (head->next == head) {
        cout << "\n=== Deleted node with ID: " << head->id << " from end ===" << endl;
        delete head;
        head = NULL;
        return;
    }

    node* x = head->prev;
    node* y = x->prev;
    cout << "\n=== Deleted node with ID: " << x->id << " from end ===" << endl;
    y->next = head;
    head->prev = y;
    delete x;
}

//********************** DELETE AT POSITION **********************
void del_at_pos(int place) {
    num();
    if (place <= 0  place > count) {
        cout << "\n!!! Wrong index - Position out of range !!!" << endl;
        return;
    }

    if (head == NULL) {
        cout << "\n!!! Nothing to delete - List is empty !!!" << endl;
        return;
    }

    if (place == 1) {
        del_at_beg();
        return;
    }

    node* x = head;
    for (int i = 1; i < place - 1; i++) {
        x = x->next;
    }
    node* z = x->next;
    cout << "\n=== Deleted node with ID: " << z->id << " from position " << place << " ===" << endl;
    x->next = z->next;
    z->next->prev = x;
    delete z;
}

//********************** MAIN FUNCTION WITH MENU **********************
int main() {
    int choice, place;
    int id;
    string name, department;
    do {
        cout << "\n================================================" << endl;
        cout << "   DOUBLY CIRCULAR LINKED LIST MENU" << endl;
        cout << "================================================" << endl;
        cout << " 1. Add at Beginning" << endl;
        cout << " 2. Add at End" << endl;
        cout << " 3. Add at Position" << endl;
        cout << " 4. Delete at Beginning" << endl;
        cout << " 5. Delete at End" << endl;
        cout << " 6. Delete at Position" << endl;
        cout << " 7. Display List" << endl;
        cout << " 0. Exit" << endl;
        cout << "================================================" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "\n--- Add at Beginning ---" << endl;
                cout << "Enter ID: ";
                cin >> id;
                cout << "Enter Name (letters only): ";
                cin >> name;
                cout << "Enter Department: ";
                cin >> department;
                add_at_beg(id, name, department);
                display();
                break;

            case 2:
                cout << "\n--- Add at End ---" << endl;
                cout << "Enter ID: ";
                cin >> id;
                cout << "Enter Name (letters only): ";
                cin >> name;
                cout << "Enter Department: ";
                cin >> department;
                add_at_end(id, name, department);
                display();
                break;

            case 3:
                cout << "\n--- Add at Position ---" << endl;
                cout << "Enter ID: ";
                cin >> id;
                cout << "Enter Name (letters only): ";
                cin >> name;
                cout << "Enter Department: ";
                cin >> department;
                cout << "Enter Position: ";
                cin >> place;
                add_at_pos(id, name, department, place);
                display();
                break;

            case 4:
                cout << "\n--- Delete at Beginning ---" << endl;
                del_at_beg();
                display();
                break;

            case 5:
                cout << "\n--- Delete at End ---" << endl;
                del_at_end();
                display();
                break;

            case 6:
                cout << "\n--- Delete at Position ---" << endl;
                cout << "Enter Position: ";
                cin >> place;
                del_at_pos(place);
                display();
                break;

            case 7:
                display();
                break;

            case 0:
                cout << "\nExiting program... Goodbye!" << endl;
                break;

            default:
                cout << "\n!!! Invalid choice! Please try again. !!!" << endl;
                break;
        }
    } while (choice != 0);

    return 0;
}