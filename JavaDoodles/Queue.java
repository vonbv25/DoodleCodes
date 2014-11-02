import java.util.Iterator;
public class Queue implements Iterable<Object> {
private int N=0;
private int tail;
private int head;
private int capacity;
private Object[] queue;

public Queue(int capacity) {
	if(capacity<0) 
		throw new IllegalArgumentException("initial capacity must be positve");
	this.capacity = capacity;
	queue = new Object[capacity];
	head = 0;
	tail = -1;
}

public void enqueue(Object n) {
	if (N >= capacity)
		throw new IllegalArgumentException("maximum capacity reached");
	tail++;
	queue[tail] = n;
	N++; 
}

public Object dequeue() {
	if (N==0) {
		head  = 0;
		tail = -1;
		throw new IllegalArgumentException("no item left");
	}
	Object remove = queue[head];
	queue[head] = null;
	head++;
	N--; 
	return remove;
}

public int size(){
	return N;
}

public boolean isEmpty() {
	return N==0;
}

public Object peek(){

	return queue[head];
}

public Iterator<Object> iterator(){
	return new ArrayIterator();
}

private class ArrayIterator implements Iterator<Object> {
	int i = 0;
	
	public boolean hasNext() {
	return i<N;
	}
	
	public Object next() {
	if (!hasNext())
		throw new IllegalArgumentException("there is no item left to iterate");
	
	Object item = queue[i];	
	i++;
	return item;		

	}
	

}




public static void main(String[] args) {

	int _a = 5;
	int _b = 6;
	Queue queue = new Queue(6);
	System.out.println("Size: " + queue.size());
	System.out.println("Enqueue " + _a + " to the queue");
	queue.enqueue(_a);
	System.out.println("Enqueue " + _b + " to the queue");
	queue.enqueue(_b);
	System.out.println("Peek the item in the first queue must be " + _a + " = " + queue.peek());
	System.out.println("Size: " + queue.size());
	System.out.println("Iterate over the queue..");
	Iterator it = queue.iterator();
	while(it.hasNext()) {
	System.out.println(it.next());

	}
		
	System.out.println("Dequeue an item from queue. must be " + _a +" = " + queue.dequeue());
	System.out.println("Peek the item in the first queue must be " + _b + " = " + queue.peek());
	System.out.println("Dequeue an item from queue. must be " + _b +" = " + queue.dequeue());	
}


}
