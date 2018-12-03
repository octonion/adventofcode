begin;

create extension if not exists fuzzystrmatch;

create schema if not exists aoc;

drop table if exists aoc.codes;

create table aoc.codes (
	code	      text
);

copy aoc.codes from '/tmp/input.txt' csv;

select c1.code,c2.code from aoc.codes c1, aoc.codes c2
where
    c1.code < c2.code
and levenshtein(c1.code,c2.code)=1;

commit;
