import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Node {
	static int TOTAL = 0;

	boolean isRaser = false;
	boolean isBat = false;

	final int index;
	final Node parent;
	final List<Node> childs = new ArrayList<>();

	public Node(int index, Node parent) {
		this.parent = parent;
		this.index = index;
	}

	void add(Node n) {
		childs.add(n);
	}

	int countRaser() {
		int count = 0;
		for (Node n : childs) {
			if (n.isRaser) {
				count++;
			} else {
				count += n.countRaser();
			}
		}
		TOTAL += count + 1;
		return count;
	}

	@Override
	public String toString() {
		final StringBuilder sb = new StringBuilder();
		sb.append(index);
		if (isRaser) {
			sb.append("레이저");
		} else {
			sb.append("쇠방망이");
		}
		sb.append("시작");
		for (Node n : childs) {
			sb.append("[");
			sb.append(n);
			sb.append("]");
		}
		sb.append(index);
		if (isRaser) {
			sb.append("레이저");
		} else {
			sb.append("쇠방망이");
		}
		sb.append("끝");
		return sb.toString();
	}
}

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String line = scan.nextLine();
		char arr[] = line.toCharArray();
		Node tree = new Node(-1, null);
		Node temp = tree;
		for (int i = 0; i < arr.length; i++) {
			char c = arr[i];
			if (c == '(') // 트리의 시작
			{
				Node n = new Node(i, temp);
				temp.add(n);
				temp = n;
			} else if (c == ')') {
				if (temp.index + 1 == i) // 레이저인경우
				{
					temp.isRaser = true;
				} else {
					temp.isBat = true;
				}
				temp = temp.parent;
			}
		}
		for (Node n : tree.childs) {
			if (n.isBat) {
				n.countRaser();
			}
		}
		System.out.println(Node.TOTAL);
	}
}