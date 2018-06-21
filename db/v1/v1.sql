CREATE DATABASE Election;

TABLE Election.Candidate (
  ID unsigned int not null PRIMARY KEY,
  FirstName varchar(256) not null,
  LastName varchar(256) not null,
  DateUp datetime not null,
  DateDown datetime default null
)

TABLE Election.Vote (
  ID unsigned int not null PRIMARY KEY,
  Reference unsigned int UNIQUE not null,
  CandidateID unsigned int default null
)

insert into Candidate(ID, FirstName, LastName, DateUp, DateDown) values (null, "Alan", "Turing", now(), null);
insert into Candidate(ID, FirstName, LastName, DateUp, DateDown) values (null, "Barbara", "Liskov", now(), null);