DROP TABLE if EXISTS TABLE_SEARCH;
DROP TABLE if EXISTS TABLE_USER;

CREATE TABLE TABLE_SEARCH (
  id integer PRIMARY KEY AUTOINCREMENT,
  search_string text not null /*,*/
 /* user_id integer not null FOREIGN key (userID) REFERENCES TABLE_USER(userID)*/
);

CREATE TABLE TABLE_USER (
  userID integer PRIMARY KEY AUTOINCREMENT,
  username varchar not null,
  password varchar not null,
  firstname varchar not null,
  lastname varchar not null
);