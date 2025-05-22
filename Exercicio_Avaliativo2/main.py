from database import Database
from teacherCRUD import TeacherCRUD

def main():
    # Initialize database connection
    db = Database("bolt://54.81.133.90:7687", "neo4j", "wills-greenwich-architecture")
    teacher_db = TeacherCRUD(db)
    
    while True:
        print("\nTeacher Management System")
        print("1. Create Teacher")
        print("2. Read Teacher")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            # Create Teacher
            print("\nCreate New Teacher")
            name = input("Name: ")
            ano_nasc = input("Year of Birth: ")
            cpf = input("CPF: ")
            teacher_db.create(name, ano_nasc, cpf)
            print(f"Teacher {name} created successfully!")
            
        elif choice == "2":
            # Read Teacher
            print("\nRead Teacher")
            name = input("Enter teacher name to search: ")
            results = teacher_db.read(name)
            if results:
                print("\nTeacher Found:")
                for teacher in results:
                    print(f"Name: {teacher['name']}")
                    print(f"Year of Birth: {teacher['ano_nasc']}")
                    print(f"CPF: {teacher['cpf']}")
            else:
                print("No teacher found with that name.")
                
        elif choice == "3":
            # Update Teacher
            print("\nUpdate Teacher")
            old_name = input("Enter current teacher name: ")
            new_cpf = input("Enter new CPF: ")
            teacher_db.update(old_name, new_cpf)
            print("Teacher updated successfully!")
            
        elif choice == "4":
            # Delete Teacher
            print("\nDelete Teacher")
            name = input("Enter teacher name to delete: ")
            teacher_db.delete(name)
            print(f"Teacher {name} deleted successfully!")
            
        elif choice == "5":
            # Exit
            print("Exiting the system...")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-5.")
    
    # Close database connection
    db.close()

if __name__ == "__main__":
    main()