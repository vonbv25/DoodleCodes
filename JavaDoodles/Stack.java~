import java.util.Iterator;

public class Stack implements Iterable<Object>{
private int N;
private Object[] stacks;
public int top;
private int capacity;

public Stack(int capacity) {
	if (capacity <= 0)
		throw new IllegalArgumentException("Must be positive");
	this.capacity = capacity;
	this.stacks = new Object[capacity];
	top = -1;
	N = 0;


}

public void push(Object n) {
	if (top>= capacity && N>= capacity)
		throw new IllegalArgumentException("maximum reached");			
	top++;
	this.stacks[top] = n;	
	this.N++;
		
}

public Object peek() {
	return stacks[top];
}

public Object pop() {
	if (top < 0){
		top = -1;
		N = 0;
		throw new IllegalArgumentException("empty");

		
	}
	Object removed = stacks[top];
	this.stacks[top] = 0;
	top--;
	N--;
	return removed;

}

public int size() {
	return N;
}

public Iterator<Object> iterator() {
	return new ArrayIterator();
}

private class ArrayIterator implements Iterator<Object>{

	private int i = N-1;
	
	public boolean hasNext() {
		return i>=0;
	}

	public Object next() {
		if (!hasNext())
			throw new IllegalArgumentException("there is no left element to iterate");
		
		Object item = stacks[i];
		i--;
		return item;	
	}


}

public static void main(String[] args) {

	int _a = 5;
	int _b = 6;
	Stack stack= new Stack(6);
	System.out.println("Size: " + stack.size());
	System.out.println("Pushes "+ _a + " to stack");
	stack.push(_a);
	System.out.println("Pushes "+ _b + " to stack");
	stack.push(_b);
	System.out.print("Peeks the value on top of stack must be "+ _b);
	System.out.print(" = "+ stack.peek());
	System.out.println();
	System.out.println("Size: " + stack.size());
	System.out.println("Iterate over the stacks..");
	Iterator iterator = stack.iterator();
	while(iterator.hasNext()) {
	System.out.println(iterator.next());
	}
	System.out.println("Pops a value from stack must be "+ _b + " = " +stack.pop());
	System.out.print("Peeks the value on top of stack must be "+ _a);
	System.out.print(" = "+ stack.peek());
	System.out.println();




}







}
