// Node Class for DoubleLinkedList
class Node {
    constructor(data) {
        this.prev = null;
        this.data = data;
        this.next = null;
    }
}

// Class DoubleLinkedList
class DoubleLinkedList {

    constructor() {
        this.head = null;
    }

    isEmpty() {
        return this.head === null;
    }

    getLength() {
        let tempNode = this.head;
        let length = 0;
        while (tempNode !== null) {
            tempNode = tempNode.next;
            length += 1;
        }
        return length;
    }

    getNodeAtPosition(position) {
        //throw Error("Not Implemented yet.");
        if (position < 0) {
            throw Error("Invalid Position.");
        }
        if (this.isEmpty()) {
            throw Error("Empty Linked List.");
        }
        let tempNode = this.head;
        while (position != 0 && tempNode.next != null) {
            position -= 1;
            tempNode = tempNode.next;
        }
        if (position !== 0) {
            throw Error("Invalid position.");
        } else {
            return tempNode;
        }
    }

    print() {
        if (this.isEmpty()) {
            return "Linked List is Empty.";
        }
        let tempNode = this.head;
        let str = "";
        const seperator = " -> ";
        while (tempNode !== null) {
            str += `${tempNode.data}${seperator}`;
            tempNode = tempNode.next;
        }
        str += "null";
        return str;
    }

    insertAtBegining(data) {
        let newNode = new Node(data);
        newNode.next = this.head;
        if (!this.isEmpty()) {
            this.head.prev = newNode;
        }
        this.head = newNode;
    }

    insertAtLast(data) {
        let newNode = new Node(data);
        if (this.isEmpty()) {
            this.head = newNode;
            return;
        }
        let traverseNode = this.head;
        while (traverseNode.next !== null) {
            traverseNode = traverseNode.next;
        }
        traverseNode.next = newNode;
        newNode.prev = traverseNode;
    }

    insertAfterNode(data, node) {
        let traverseNode = this.head;
        while (traverseNode !== node) { // Object Equality problem in JSs
            traverseNode = traverseNode.next;
        }
        let newNode = new Node(data);

    }

    insertBeforeNode(data, node) {

    }

    // position: 0 based index of the list.
    insertAtPosition(data, position) {
        if (position < 0) {
            throw Error("Invalid position.");
        } else if (position === 0) {
            this.insertAtBegining(data);
            return;
        } else if (position === this.getLength()) {
            // this allows max index + 1 entry in the linked list.
            this.insertAtLast(data);
            return;
        }
        let tempNode = this.head;
        while (position !== 0 && tempNode.next !== null) {
            position -= 1;
            tempNode = tempNode.next;
        }
        if (position !== 0) { // if the position is not zero, after the loop ends, 
            // it means that the tempNode is null. 
            // So the given position is more than the length of the linked list.
            // So it is an Invalid position.
            throw Error("Invalid Position.");
        }
        let newNode = new Node(data)
        newNode.next = tempNode;
        tempNode.prev.next = newNode;
        newNode.prev = tempNode.prev;
    }

    deleteAtBegining() {
        if (this.isEmpty()) {
            throw Error("Empty Linked List.");
        }
        let tempNode = this.head;
        this.head = this.head.next;
        tempNode.next = null;
        return tempNode;
    }

    deleteAtEnd() {
        if (this.isEmpty()) {
            throw Error("Empty Linked List.");
        }
        let traverseNode = this.head;
        while (traverseNode.next !== null) {
            traverseNode = traverseNode.next;
        }
        if (traverseNode.prev !== null) {
            traverseNode.prev.next = null; // Since deleting at last, next pointer of last node will always be null
        }
        if (this.head === traverseNode) {
            this.head = null; // if head node, reset head to null
        }
        traverseNode.next = null;
        return traverseNode;
    }

    // position: 0 based index of the list.
    deleteAtPosition(position) {
        throw Error("Not Implemented yet.");
    }
}


let dl = new DoubleLinkedList();
dl.insertAtLast(3)
dl.insertAtBegining(2)
dl.insertAtBegining(1)
dl.insertAtLast(4)
console.log(dl.print())
dl.insertAtPosition('a', 0)
console.log(dl.print())
dl.insertAtPosition('b', 2)
console.log(dl.print())
dl.insertAtPosition('c', dl.getLength() - 1)
console.log(dl.print())
dl.insertAtPosition('d', dl.getLength())
console.log(dl.print())
dl.deleteAtBegining()
console.log(dl.print())
dl.deleteAtEnd()
console.log(dl.print())