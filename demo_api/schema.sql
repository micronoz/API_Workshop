-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS borrow;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL
);

CREATE TABLE book (
  id INTEGER PRIMARY KEY,
  bookname TEXT NOT NULL
);

CREATE TABLE borrow (
  borrower_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  FOREIGN KEY (borrower_id) REFERENCES user (id),
  FOREIGN KEY (book_id) REFERENCES book (id)
);