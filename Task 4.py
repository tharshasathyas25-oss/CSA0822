from datetime import datetime
def add_returned_book(book_name, student_name):
    try:
        with open("book_log.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{datetime.now()} - {book_name} - {student_name}\n"
            )
        print("Book return recorded successfully.")
    except (OSError, UnicodeError) as error:
        with open("error_log.txt", "a", encoding="utf-8") as log:
            log.write(f"{datetime.now()} - {error}\n")
        print("Error occurred. Check error_log.txt")
add_returned_book("Python Programming", "Ravi")
add_returned_book("Data Structures", "Priya")