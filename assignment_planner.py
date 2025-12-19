
#Assignment Planner
#CSCI 120 Final Project

#This program allows users to:
#- Add courses
#- Add assignments with due dates
#- View upcoming assignments
#- Mark assignments as complete


from datetime import datetime


class Assignment:
    #Represents a single assignment

    def __init__(self, name, due_date, priority):
        #Initialize an assignment.
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        #Mark the assignment as completed
        self.completed = True

    def __str__(self):
        #Return a readable string representation of the assignment
        status = "✓" if self.completed else "✗"
        return f"{self.name} | Due: {self.due_date.date()} | Priority: {self.priority} | Done: {status}"


class Course:
    #Represents a course containing multiple assignments
    def __init__(self, course_name):
        #Initialize a course
        self.course_name = course_name
        self.assignments = []

    def add_assignment(self, assignment):
        #Add an assignment to the course
        self.assignments.append(assignment)

    def get_pending_assignments(self):
        #Return a list of assignments that are not completed
        return [a for a in self.assignments if not a.completed]


class AssignmentPlanner:
    #Main planner that manages multiple courses

    def __init__(self):
        #Initialize the planner
        self.courses = {}

    def add_course(self, course_name):
        #Add a new course to the planner
        if course_name not in self.courses:
            self.courses[course_name] = Course(course_name)
            print(f"Course '{course_name}' added.")
        else:
            print("Course already exists.")

    def add_assignment(self, course_name, name, due_date, priority):
        #Add an assignment to a course
        if course_name in self.courses:
            assignment = Assignment(name, due_date, priority)
            self.courses[course_name].add_assignment(assignment)
            print("Assignment added.")
        else:
            print("Course not found.")

    def list_assignments(self):
        #List all assignments sorted by due date and priority
        all_assignments = []

        for course in self.courses.values():
            for assignment in course.assignments:
                all_assignments.append((course.course_name, assignment))

        all_assignments.sort(key=lambda x: (x[1].due_date, x[1].priority))

        for course_name, assignment in all_assignments:
            print(f"[{course_name}] {assignment}")

    def mark_assignment_complete(self, course_name, assignment_name):
        #Mark a specific assignment as completed
        if course_name in self.courses:
            for assignment in self.courses[course_name].assignments:
                if assignment.name == assignment_name:
                    assignment.mark_complete()
                    print("Assignment marked complete.")
                    return
            print("Assignment not found.")
        else:
            print("Course not found.")


def main():
    #Main menu loop for interacting with the assignment planner
    planner = AssignmentPlanner()

    while True:
        print("\nAssignment Planner Menu")
        print("1. Add course")
        print("2. Add assignment")
        print("3. View all assignments")
        print("4. Mark assignment complete")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            course_name = input("Course name: ")
            planner.add_course(course_name)

        elif choice == "2":
            course_name = input("Course name: ")
            name = input("Assignment name: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            priority = int(input("Priority (1 = highest): "))
            planner.add_assignment(course_name, name, due_date, priority)

        elif choice == "3":
            planner.list_assignments()

        elif choice == "4":
            course_name = input("Course name: ")
            assignment_name = input("Assignment name: ")
            planner.mark_assignment_complete(course_name, assignment_name)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()