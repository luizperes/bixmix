echo "SQLite 'abc%'"

time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB1 WHERE description LIKE 'abc%'" > jaca
time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB2 WHERE description LIKE 'abc%'" > jaca
time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB3 WHERE description LIKE 'abc%'" > jaca
time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB4 WHERE description LIKE 'abc%'" > jaca
time ./sqlite/sqlite3 ./sqlite/j "SELECT * FROM TB5 WHERE description LIKE 'abc%'" > jaca


echo "Postgres 'abc%'"

time psql -d j -c "SELECT * FROM TB1 WHERE description LIKE 'abc%'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB2 WHERE description LIKE 'abc%'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB3 WHERE description LIKE 'abc%'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB4 WHERE description LIKE 'abc%'" --csv -o jaca
time psql -d j -c "SELECT * FROM TB5 WHERE description LIKE 'abc%'" --csv -o jaca

echo "Parabix 'abc%'"

time ~/Projects/parabix-devel/build/bin/icgrep "abc.*" out/10en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep "abc.*" out/50en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep "abc.*" out/100en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep "abc.*" out/500en > /dev/null
time ~/Projects/parabix-devel/build/bin/icgrep "abc.*" out/1000en > /dev/null
