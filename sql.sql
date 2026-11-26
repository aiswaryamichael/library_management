create database library_management;

use library_management;

create table books(book_id int Primary key not null auto_increment,
				   title varchar(20),
                   author varchar(20),
                   category varchar(20),
                   total_copies int,
                   available_copies int);
                   
select * from books;
