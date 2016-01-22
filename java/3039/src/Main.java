import java.util.*;

class Student {

	int id;
	int understand;
	int knowledge;

	public Student(int id, int understand, int knowledge) {
		this.id = id;
		this.understand = understand;
		this.knowledge = knowledge;
	}
}

public class Main {
	private static int MAX_KNOWLEDGE = 0;
	private static volatile int ID_GENERATOR = 1;
	private static final Scanner scan = new Scanner(System.in);
	private static final ArrayList<Integer> knowledgeList = new ArrayList<>();
	private static final HashMap<Integer, Student> studentsById = new HashMap<>();
	private static final HashMap<Integer, HashSet<Student>> studentsByKnowledge = new HashMap<>();

	public static void main(String[] args) {
		int n = scan.nextInt();
		for (int i = 0; i < n; i++) {
			String situation = scan.next();
			if (situation.equals("D")) {
				int undetstand = scan.nextInt();
				int knowledge = scan.nextInt();
				Student student = new Student(ID_GENERATOR++, undetstand, knowledge);
				studentsById.put(student.id, student);
				if (studentsByKnowledge.containsKey(knowledge)) {
					studentsByKnowledge.get(knowledge).add(student);
				} else {
					HashSet<Student> studentHashSet = new HashSet<>();
					studentHashSet.add(student);
					studentsByKnowledge.put(knowledge, studentHashSet);
					if (knowledge > MAX_KNOWLEDGE) {
						MAX_KNOWLEDGE = knowledge;
					}
					knowledgeList.add(knowledge);
					knowledgeList.sort(new Comparator<Integer>() {
						@Override
						public int compare(Integer o1, Integer o2) {
							if (o1 < o2) {
								return -1;
							} else {
								return 1;
							}
						}
					});
				}
			} else {
				int id = scan.nextInt();
				Student student = studentsById.get(id);
				int current = knowledgeList.indexOf(student.knowledge);
				HashSet<Student> targetSet = studentsByKnowledge.get(current);
				if (targetSet.size() == 1) {
					targetSet = studentsByKnowledge.get(knowledgeList.get(current + 1));
				}

				if (targetSet == null || targetSet.size() == 0) {
					System.out.println("NE");
					return;
				}

				Student target = null;
				Iterator<Student> candidates = targetSet.iterator();
				while (candidates.hasNext()) {
					Student candidate = candidates.next();
					if (candidate.understand >= student.understand) {
						if (target == null) {
							target = candidate;
						} else {
							if ((candidate.understand < target.understand)) {
								target = candidate;
							}
						}
					}
				}
				if (target == null) {
					System.out.println("NE");
				} else {
					System.out.println(target.id);
				}
			}
		}
	}
}
