# Library Management Tool

This is a simple Python library management tool that allows you to manage books and authors. You can perform various operations such as adding authors, adding books, deleting books, deleting authors, searching for books by author, searching for authors by name, and exporting the library data to a CSV file.

### Options

- **1. Add Author:** You can add an author to the library by providing the author's name and email.

- **2. Add Book:** You can add a book to the library by providing the book's name and either the index or name of the author. If the author does not exist, you can also add the author's name and email.

- **3. Delete Book at Index:** You can delete a book from the library by specifying its index.

- **4. Delete Author at Index:** You can delete an author from the library by specifying their index.

- **5. Find Book by Author:** You can search for a book by providing a keyword related to the author's name. The tool will display the index of the books with matching author names.

- **6. Find Author by Name:** You can search for an author by providing a keyword related to the author's name. The tool will display the index of the authors with matching names.

- **7. Export Library:** You can export the library data to a CSV file named 'filename.csv', which includes information about book names, author names, and author emails.

## Sample Usage

Here's a sample scenario of how you can use the tool:

1. Select option 1 to add an author by providing their name and email.

2. Select option 2 to add a book, and either provide the author's index or name.

3. Continue adding authors and books as needed.

4. You can search for books or authors or export the library data as required.

5. To exit the tool, press 'n' when asked if you want to continue.

## Dependencies

This code uses the `pandas` library for exporting data to a CSV file. Make sure you have `pandas` installed in your Python environment.

You can install it using pip: pip install pandas


## Author

This tool was created by Parag Gupta

Feel free to modify and enhance it according to your requirements.

Enjoy managing your library with this simple tool!


